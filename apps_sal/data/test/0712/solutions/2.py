__author__ = 'PrimuS'
import decimal
decimal.getcontext().prec = 1000
inp = input().split()
n = int(inp[0])
p = decimal.Decimal(inp[1])
t = int(inp[2])
facs = {}
ps = {}
p1s = {}
facs[0] = decimal.Decimal(1)
ps[0] = decimal.Decimal(1)
p1s[0] = decimal.Decimal(1)
for i in range(1, max(n, t) + 1):
    facs[i] = facs[i - 1] * decimal.Decimal(i)
    ps[i] = ps[i - 1] * p
    p1s[i] = p1s[i - 1] * (1 - p)


def c(n, k):
    return facs[n] / facs[n - k] / facs[k]


res = decimal.Decimal(0)
up = min(n, t)
if n < t:
    up = n - 1
for i in range(1, up + 1):
    cur = decimal.Decimal(i)
    cur *= c(t, i)
    cur *= ps[i]
    cur *= p1s[t - i]
    res += cur
if n < t:
    cur2 = t
    while cur2 >= n:
        cur = decimal.Decimal(n)
        cur *= c(cur2 - 1, n - 1)
        cur *= ps[n]
        cur *= p1s[cur2 - n]
        res += cur
        cur2 -= 1
print(res)
