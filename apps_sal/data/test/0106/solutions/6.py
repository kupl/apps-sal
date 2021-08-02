n, m, k = map(int, input().split())
a, b = map(int, input().split())
a -= 1
b -= 1
an = a // (m * k)
am = (a % (m * k)) // k
bn = b // (m * k)
bm = (b % (m * k)) // k
res = 0
n -= 1
if an != bn:
    res = res + min(10 + bm, bm * 5) + min(10 + am, am * 5)
    if an < bn:
        res = res + (min(bn - an, n - bn + an + 1)) * 15
    else:
        res = res + (min((an - bn), bn + n - an + 1)) * 15
else:
    x = abs(bm - am)
    res = res + min(10 + x, x * 5)
print(res)
