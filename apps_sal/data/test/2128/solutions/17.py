mod = 998244353


def inv_mod(n):
    return pow(n, mod - 2, mod)


n = int(input())
p = [int(x) for x in input().split()]

res = 0
for i in p:
    res = (res + 1) * 100 * inv_mod(i) % mod

print(res)
