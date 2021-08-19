import heapq
import sys
input = sys.stdin.readline
(N, Q) = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]
CD = [tuple(map(int, input().split())) for _ in range(Q)]
H = 2 * 10 ** 5
INF = 10 ** 18
rates = [[] for _ in range(H)]
members = [set() for _ in range(H)]
belongs = [-1] * N
for (i, (a, b)) in enumerate(AB):
    b -= 1
    heapq.heappush(rates[b], (-a, i))
    members[b].add(i)
    belongs[i] = b
mxrates = []
for (num, r) in enumerate(rates):
    if len(r) > 0:
        heapq.heappush(mxrates, (-r[0][0], num))
for (c, d) in CD:
    (c, d) = (c - 1, d - 1)
    old = belongs[c]
    belongs[c] = d
    members[old].remove(c)
    members[d].add(c)
    while len(rates[old]) > 0 and rates[old][0][1] not in members[old]:
        heapq.heappop(rates[old])
    if len(rates[old]) > 0:
        heapq.heappush(mxrates, (-rates[old][0][0], old))
    heapq.heappush(rates[d], (-AB[c][0], c))
    heapq.heappush(mxrates, (AB[c][0], d))
    while mxrates:
        (rate, num) = mxrates[0]
        if len(rates[num]) == 0 or -rates[num][0][0] != rate:
            heapq.heappop(mxrates)
        else:
            print(rate)
            break
