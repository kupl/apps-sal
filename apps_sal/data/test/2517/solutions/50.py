from itertools import permutations
from scipy.sparse.csgraph import floyd_warshall
INF = 10 ** 18
(N, M, R) = map(int, input().split())
r = list(map(int, input().split()))
dp = [[INF for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            dp[i][j] = 0
for i in range(M):
    (a, b, c) = map(int, input().split())
    dp[a - 1][b - 1] = c
    dp[b - 1][a - 1] = c
wf = floyd_warshall(dp)
ans = INF
for i in permutations(r):
    tmp = 0
    for j in range(1, len(i)):
        tmp += wf[i[j - 1] - 1][i[j] - 1]
    ans = min(ans, tmp)
print(int(ans))
