cost = [-1, 2, 5, 5, 4, 5, 6, 3, 7, 6]
N, M = map(int, input().split())
A = list(map(int, input().split()))

dp = [None] * (N + 1)
dp[0] = ''

for i in range(1, N + 1):
    for a in A:
        if i - cost[a] >= 0 and dp[i - cost[a]] != None:
            s = dp[i - cost[a]] + str(a)
            if dp[i] == None or len(dp[i]) < len(s):
                dp[i] = s
            elif len(dp[i]) > len(s):
                continue
            else:
                dp[i] = max(dp[i], s)


print(dp[N])
