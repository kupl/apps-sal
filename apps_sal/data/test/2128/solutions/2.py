mod = 998244353


def inv_mod(n):
    return pow(n, mod - 2, mod)


def frac_mod(a, b):
    return a * inv_mod(b) % mod


n = int(input())
a = input().split()
res = 0
for v in a:
    res = (res + 1) * 100 * inv_mod(int(v)) % mod
print(res)
