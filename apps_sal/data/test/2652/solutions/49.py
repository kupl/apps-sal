from heapq import heappop, heappush
import sys
sys.setrecursionlimit(10 ** 6)
n = int(input())
pair = [i for i in range(n)]
que = []
e = [None] * n
for i in range(n):
    (x, y) = map(int, input().split())
    e[i] = (i, x, y)
ex = sorted(e, key=lambda x: x[1])
ey = sorted(e, key=lambda x: x[2])
for i in range(n - 1):
    w = ex[i + 1][1] - ex[i][1]
    heappush(que, (w, ex[i][0], ex[i + 1][0]))
for i in range(n - 1):
    w = ey[i + 1][2] - ey[i][2]
    heappush(que, (w, ey[i][0], ey[i + 1][0]))


def find(x):
    if x == pair[x]:
        return x
    else:
        tmp = find(pair[x])
        pair[x] = tmp
        return tmp


q = []
ans = 0
while que:
    (w, s, t) = heappop(que)
    root_s = find(s)
    root_t = find(t)
    if root_s != root_t:
        pair[root_s] = root_t
        ans += w
print(ans)
