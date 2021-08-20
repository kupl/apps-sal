n = int(input())
c = [input() for _ in range(4)]
mod = pow(10, 9) + 7
d = dict()
d['AA'] = c[0]
d['AB'] = c[1]
d['BA'] = c[2]
d['BB'] = c[3]
now = set()
now.add('AB')
dp = [1] * max(n + 1, 4)
for i in range(1, 4):
    x = list(now)
    now0 = set()
    for y in x:
        for j in range(i):
            z = list(y)
            z.insert(j + 1, d[z[j] + z[j + 1]])
            now0.add(''.join(z))
    dp[i] = len(list(now0))
    now = now0
if dp[3] == 3:
    for i in range(4, max(n + 1, 4)):
        dp[i] = dp[i - 1] + dp[i - 2]
        dp[i] %= mod
if dp[3] == 4:
    for i in range(4, max(n + 1, 4)):
        dp[i] = 2 * dp[i - 1]
        dp[i] %= mod
ans = dp[n - 2]
print(ans)
