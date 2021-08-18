import queue
def intput(): return list(map(int, input().split()))


N, M, K = intput()
ht = [[] for _ in range(N)]
for _ in range(N):
    day = input()
    ht[_] = [i for i in range(M) if day[i] == '1']


tc = [1, 2, 3, 8, 9]
req = [[0 for _ in range(M + 1)] for __ in range(N)]
dp = [[0 for _ in range(K + 1)] for __ in range(N)]
for i in range(N):
    for j in range(len(ht[i])):
        req[i][j] = ht[i][-1] - ht[i][0] + 1
        for first in range(j + 1):
            last = first + len(ht[i]) - j - 1
            cost = ht[i][last] - ht[i][first] + 1
            if last >= first:
                req[i][j] = min(req[i][j], cost)

for i in range(min(len(req[0]), len(dp[0]))):
    dp[0][i] = req[0][i]
for i in range(1, N):
    for j in range(K + 1):
        dp[i][j] = dp[i - 1][j] + req[i][0]
        for z in range(1 + min(j, len(ht[i]))):
            dp[i][j] = min(dp[i][j], dp[i - 1][j - z] + req[i][z])

print(dp[-1][-1])
