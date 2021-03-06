import os
import sys
import numpy as np
if os.getenv('LOCAL'):
    sys.stdin = open('_in.txt', 'r')
sys.setrecursionlimit(2147483647)
INF = float('inf')
IINF = 10 ** 18
MOD = 10 ** 9 + 7
(N, M) = list(map(int, sys.stdin.readline().split()))
ST = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
graph = [[] for _ in range(N + 1)]
for (s, t) in ST:
    graph[s].append(t)
dp = np.full((N + 1, N + 1), IINF, dtype=float)
dp[N] = 0.0
for v in reversed(list(range(1, N))):
    dp[v, :] = dp[graph[v], :].sum(axis=0) / len(graph[v]) + 1
    if len(graph[v]) >= 2:
        s = dp[graph[v], v].sum() - dp[graph[v], v].max()
        dp[v, v] = s / (len(graph[v]) - 1) + 1
print(dp[1].min())
