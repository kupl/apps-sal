import sys

inf = float("inf")

mod, MOD = 1000000007, 998244353


def get_array(): return list(map(int, sys.stdin.readline().strip().split()))
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def input(): return sys.stdin.readline().strip()


def is_beautiful(sum):
    if sum == 0:
        return 0
    while sum:
        if sum % 10 != a:
            if sum % 10 != b:
                return 0
        sum //= 10
    return 1


def nCr(n, r):
    return (fact[n] * invfact[r] * invfact[n - r]) % mod


fact = [0] * (1000005)
invfact = [0] * (1000005)
fact[0] = fact[1] = invfact[0] = invfact[1] = 1
for i in range(1, 1000003):
    fact[i] = (fact[i - 1] % mod * i % mod) % mod
invfact[1000000] = pow(fact[1000000], mod - 2, mod)
for i in range(999999, 0, -1):
    invfact[i] = (invfact[i + 1] % mod * (i + 1) % mod) % mod

a, b, n = get_ints()
if a == b:
    if is_beautiful(a * n):
        print(1)
    else:
        print(0)
ans = 0
for i in range(n + 1):
    if is_beautiful(a * i + b * (n - i)):
        ans += nCr(n, i)
ans %= mod
print(ans)
