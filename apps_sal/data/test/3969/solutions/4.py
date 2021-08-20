"""n, m, k = [int(x) for x in input().split()]

trees = tuple([int(x) for x in input().split()])

costs = []
for x in range(n):
    costs.append([0] + [int(x) for x in input().split()])

dp = [[[float('inf') for z in range(m + 1)] for y in range(k + 1)] for x in range(n)]

if trees[0] == 0:
    for k in range(len(dp[0][0])):
        dp[0][1][k] = cost[0][k]
else:
    dp[0][0][trees[0]] = cost[0][trees[0]]

for i in range(1, len(dp)):
    for j in range(1, len(dp[0])):
        for k in range(1, len(dp[0][0])):
            if trees
            for l in range(len(dp[0][0])):
                if k == l:
                    dp[i][j][k] = dp[i - 1][j][k] + cost[i][k]
                else:
                    dp[i][j][k] = dp[i - 1][j - 1][l] + cost[i][k]"""
(n, m) = [int(x) for x in input().split()]
plant = [int(input().split()[0]) for x in range(n)]
dp = [1 for x in range(n)]
for i in range(len(plant)):
    for j in range(0, i):
        if plant[j] > plant[i]:
            continue
        dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))
'for i in range(1, n):\n    for k in range(plant[i], 0, -1):\n        dp[plant[i]] = max(dp[plant[i]], 1 + dp[k])\nprint(n - max(dp) - 1)'
