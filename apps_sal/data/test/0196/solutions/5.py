(x, k) = map(int, input().split())
ans = 0
md = 1000000007


def bpow(base, exp, md):
    if exp == 0:
        return 1
    if exp % 2 == 1:
        return base * bpow(base, exp - 1, md) % md
    else:
        k = bpow(base, exp // 2, md)
        return k * k % md


pw = bpow(2, k, md)
ans = 2 * pw * x % md
if x != 0:
    ans -= pw - 1
ans = (ans + md) % md
print(ans)
