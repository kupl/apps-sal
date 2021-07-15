N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

dp = [0] * (N+1)

t = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]

for i in range(1, N+1):
    for a in A:
        if 0 <= i-t[a]:     
            if dp[i-t[a]] == 0 and i-t[a] > 0: continue
            dp[i] = max(dp[i], dp[i-t[a]]*10+a)
print(dp[N])
