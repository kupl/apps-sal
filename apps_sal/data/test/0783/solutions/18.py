n = int(input())
lst = list(map(int, input().split()))
dp = [-1000] * n
dp[n - 1] = 0
for i in range(len(lst) - 2, -1, -1):
    dp[i] = max(dp[i + 1], lst[i + 1])
for i in range(n):
    if dp[i] >= lst[i]:
        print(dp[i] - lst[i] + 1, end=' ')
    else:
        print(0, end=' ')
        

           

