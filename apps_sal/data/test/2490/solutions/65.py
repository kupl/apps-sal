s = input()
s = s[::-1]
s += '0'
ans = 0
dp = [0, 10 ** 9]
for c in s:
    i = int(c)
    a = dp[0] + i
    if i < 9 and a > dp[1] + i + 1:
        a = dp[1] + i + 1
    b = dp[1] + 9 - i
    if i > 0 and b > dp[0] + 10 - i:
        b = dp[0] + 10 - i
    dp = [a, b]
print(dp[0])
