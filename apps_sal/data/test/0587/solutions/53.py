import heapq
from operator import itemgetter
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
TD = sorted([list(map(int, input().split())) for _ in range(n)], reverse=True, key=itemgetter(1))
L = [[] for _ in range(n + 1)]
P = []
a = 0
cnt = 0
F = [-float("inf")] * (n + 1)
for t, d in TD[:k]:
    L[t].append(d)
    if len(L[t]) == 1:
        a += 1
    cnt += d
F[a] = cnt
for i in range(1, n + 1):
    while len(L[i]) > 1:
        heapq.heappush(P, L[i].pop())
now = k
for i in range(a, n):
    if len(P) == 0:
        break
    while now < n and L[TD[now][0]]:
        now += 1
    if now == n:
        break
    t, d = TD[now]
    L[t].append(d)
    F[i + 1] = F[i] - heapq.heappop(P) + d
ans = 0
for i in range(a, n + 1):
    ans = max(ans, F[i] + i * i)
print(ans)
