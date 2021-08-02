mod = 10**9 + 7
X, Y = list(map(int, input().split()))

if (X + Y) % 3 != 0:
    print((0))
    return

a = (2 * Y - X) // 3
b = (2 * X - Y) // 3
if a < 0 or b < 0:
    print((0))
    return

m = min(a, b)

ifact = 1
for i in range(2, m + 1):
    ifact = (ifact * i) % mod
ifact = pow(ifact, mod - 2, mod)
fact = 1
for i in range(a + b, a + b - m, -1):
    fact = (fact * i) % mod

print((fact * ifact % mod))
