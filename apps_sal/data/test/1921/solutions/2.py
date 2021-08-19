from operator import itemgetter
import heapq
import sys
input = sys.stdin.readline
(n, m) = list(map(int, input().split()))
(sx, sy, fx, fy) = list(map(int, input().split()))
W = [list(map(int, input().split())) + [i] for i in range(m)] + [[sx, sy, m]]
ANS = [n ** 2]


def ans(time, x, y):
    ANS[0] = min(ANS[0], time + abs(fx - x) + abs(fy - y))


WX = sorted(W, key=itemgetter(0))
WY = sorted(W, key=itemgetter(1))
EDGE = [[] for i in range(m + 1)]
TIME = [1 << 60] * (m + 1)
TIME[m] = 0
for i in range(1, m + 1):
    (x0, y0, m0) = WX[i - 1]
    (x1, y1, m1) = WX[i]
    EDGE[m0].append((m1, min(abs(x0 - x1), abs(y0 - y1))))
    EDGE[m1].append((m0, min(abs(x0 - x1), abs(y0 - y1))))
    (x0, y0, m0) = WY[i - 1]
    (x1, y1, m1) = WY[i]
    EDGE[m0].append((m1, min(abs(x0 - x1), abs(y0 - y1))))
    EDGE[m1].append((m0, min(abs(x0 - x1), abs(y0 - y1))))
Q = [(0, m)]
while Q:
    (time, town) = heapq.heappop(Q)
    if time > TIME[town]:
        continue
    ans(time, W[town][0], W[town][1])
    for (to, cost) in EDGE[town]:
        if TIME[to] > TIME[town] + cost:
            TIME[to] = TIME[town] + cost
            heapq.heappush(Q, (TIME[to], to))
print(ANS[0])
