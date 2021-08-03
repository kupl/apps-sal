import sys
from itertools import accumulate
N, K = map(int, input().split())
G = [[1 if s == 'B' else 0 for s in sys.stdin.readline().strip()] for _ in range(N)]

Ans = [[0] * (N + 1) for _ in range(N + 1)]
ans = 0

for i in range(N):
    g = G[i]
    if 1 not in g:
        ans += 1
        continue
    r = g.index(1)
    l = max(0, N - K - g[::-1].index(1))
    j = max(0, i - K + 1)
    if l <= r:
        Ans[j][l] += 1
        Ans[j][r + 1] -= 1
        Ans[i + 1][l] -= 1
        Ans[i + 1][r + 1] += 1

G = list(map(list, zip(*G)))
Ans = list(map(list, zip(*Ans)))

for i in range(N):
    g = G[i]
    if 1 not in g:
        ans += 1
        continue
    r = g.index(1)
    l = max(0, N - K - g[::-1].index(1))
    j = max(0, i - K + 1)
    if l <= r:
        Ans[j][l] += 1
        Ans[j][r + 1] -= 1
        Ans[i + 1][l] -= 1
        Ans[i + 1][r + 1] += 1

Ans = [list(accumulate(g))[::-1] for g in Ans]
Ans = list(map(list, zip(*Ans)))
Ans = [list(accumulate(g))[::-1] for g in Ans]

print(ans + max(max(g) for g in Ans))
