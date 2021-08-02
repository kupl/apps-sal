s = input()
p = 10**9 + 7
a = []
#ind = []
#k = -1
for ch in s:
    if ch == 'a':
        if len(a) == 0 or a[-1][1] == True:
            a += [(1, False)]
        else:
            a[-1] = (a[-1][0] + 1, False)
    if ch == 'b' and len(a) > 0:
        a[-1] = (a[-1][0], True)
n = len(a)
dp = {}
dp[n] = 1
for i in range(n - 1, -1, -1):
    dp[i] = (dp[i + 1] * (1 + a[i][0])) % p
print((dp[0] - 1) % p)
