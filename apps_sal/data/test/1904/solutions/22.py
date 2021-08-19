l = int(input())
s = input()
arr = list(map(int, input().split()))
hard = 'hard'
dp = [0] * 4
for i in range(l):
    if s[i] == hard[0]:
        dp[0] += arr[i]
    for j in range(1, 4):
        if s[i] == hard[j]:
            dp[j] = min(dp[j - 1], dp[j] + arr[i])
print(min(dp))
