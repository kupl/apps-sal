import math
n = int(input())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7


def lcm(a, b):
    return a * b // math.gcd(a, b)


l = a[0]
for i in range(n):
    l = lcm(l, a[i])
l %= mod
ans = 0
for i in range(n):
    inv = pow(a[i], mod - 2, mod)
    ans += l * inv % mod
print(ans % mod)
