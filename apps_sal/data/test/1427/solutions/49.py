def gcd(m, n):
    r = m % n
    return gcd(n, r) if r else n


def lcm(m, n):
    return m // gcd(m, n) * n


MOD = 10**9 + 7
n = int(input())
a = list(map(int, input().split()))
l = a[0]
for x in a[1:]:
    l = lcm(x, l)

l %= MOD

ans = 0
for x in a:
    ans += l * pow(x, MOD - 2, MOD) % MOD
print((ans % MOD))
