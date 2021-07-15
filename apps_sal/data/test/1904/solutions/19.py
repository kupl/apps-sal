_ = input()
s = input()
a = list(map(int, input().split()))

hard = "hard"

dp = [0]*4
for i in range(len(s)):
    if s[i] == hard[0]:
        dp[0] += a[i]
    for j in range(1, 4):
        if s[i] == hard[j]:
            # If same letter, either leave as-is (extend prefix) or remove it
            dp[j] = min(dp[j-1], dp[j] + a[i])

print(min(dp))

