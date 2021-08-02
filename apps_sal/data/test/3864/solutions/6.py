mod = 998244353

n = int(input())
half = 499122177 * n % mod
d = pow(2, mod - n, mod)
h = (n + 1) // 2
ans = [half] * h
for i in range(h - 2):
    ans[i + 2] = ans[i + 1] + (2 * i + 3) * d
    ans[i + 2] %= mod
    d *= 4
    d %= mod
for i in range(h):
    print((ans[i]))
if n % 2 == 0:
    print((ans[-1]))
for i in range(2, h + 1):
    print((ans[-i]))
