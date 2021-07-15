N, M = list(map(int, input().split()))
A = tuple(map(int, input().split()))

M_lst = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]

dp = [-1] * (N + 10)
dp[0] = 0
for i in range(N + 1):
    if dp[i] == -1:
        continue
    for a in A:
        dp[i + M_lst[a]] = max(dp[i + M_lst[a]], dp[i] * 10 + a)
print((dp[N]))

