dpc = [1]
dpci = []
for i in range(1, 2000):
    dpc.append((dpc[i - 1] * i) % 1000000007)


def modInverse(a, m):
    m0 = m
    y = 0
    x = 1
    if (m == 1):
        return 0
    while (a > 1):
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if (x < 0):
        x = x + m0
    return x


for i in dpc:
    dpci.append(modInverse(i, 1000000007))


def c(n, r):
    if(r < 0):
        return 0
    if(n < r):
        return 0
    if(n < 0):
        return 0
    return dpc[n] * dpci[r] * dpci[n - r]


dp = {1: 0}


def f(n):
    x = n
    b = 0
    while x != 0:
        x = x & (x - 1)
        b += 1
    dp[n] = dp[b] + 1


for i in range(2, 1001):
    f(i)
a = [[], [], [], [], []]
for i in dp:
    a[dp[i]].append(i)
n = input()
l = len(n)
x = []
for i in range(l):
    if n[i] == '1':
        x.append(i)
k = int(input())
if k > 5:
    print(0)
elif k == 0:
    print(1)
else:
    ans = 0
    for i in a[k - 1]:
        r = 0
        for j in x:
            if i - r < 0:
                break
            xy = c(l - j - 1, i - r)
            ans = (ans + xy) % 1000000007
            r += 1
    if len(x) in a[k - 1] and len(x) != 1:
        ans += 1
    if len(x) > 1 and k == 1:
        ans -= 1
    print(ans)
