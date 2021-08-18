MOD = 10**9 + 7
n, m = map(int, input().split())
xlist = list(map(int, input().split()))
ylist = list(map(int, input().split()))

x0, y0 = xlist[0], ylist[0]
for i in range(n):
    xlist[i] -= x0
for i in range(m):
    ylist[i] -= y0

xsum = 0
for i in range(1, n):
    xsum += xlist[i] * i
    xsum -= xlist[i] * (n - i - 1)
    xsum %= MOD

ysum = 0
for i in range(1, m):
    ysum += ylist[i] * i
    ysum -= ylist[i] * (m - i - 1)
    ysum %= MOD

print((xsum * ysum) % MOD)
