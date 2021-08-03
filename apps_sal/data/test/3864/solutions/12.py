mo = 998244353

n = int(input())

if n == 1:
    print(pow(2, mo - 2, mo))
    return


def calc(n, s):
    nonlocal bans, qa
    return (bans + qa(2, min(n - 2, 2 * n - 1 - 2 * s, 2 * s - 2))) % mo


a = [0] * n

for k in range(3, n - 1, 2):
    a[k] = k * pow(2, k - 2, mo) % mo

for k in range(1, n):
    a[k] += a[k - 1]


def qa(l, r):
    if l > r:
        return 0
    return a[r] - a[l - 1]


bans = 0
bans = (bans + pow(2, n - 2, mo) * n) % mo
for i in range(1, n):
    bans = (bans + 2 * i) % mo
tmp = 0
for k in range(2, n - 1):
    tmp = (tmp + pow(2, n - k - 2, mo) * (k - 1)) % mo
bans = (bans + tmp * n) % mo

dom = pow(2, -n + mo - 1, mo)

for s in range(1, n + 1):
    print(calc(n, s) * dom % mo)
