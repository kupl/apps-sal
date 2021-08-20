n = int(input())
s = input()
ai = list(map(int, input().split()))
a = ord('a')
e = 10 ** 9 + 7
dp = [1] + [0] * n
dp2 = [0] * (n + 1)
l = 0
for i in range(1, n + 1):
    dp2[i] = n
    f = i - 1
    ma = 10000
    while f >= 0:
        ma = min(ma, ai[ord(s[f]) - a])
        if ma < i - f:
            break
        dp[i] = (dp[i] + dp[f]) % e
        dp2[i] = min(dp2[i], dp2[f] + 1)
        l = max(l, i - f)
        f -= 1
print(dp[n], l, dp2[n], sep='\n')
