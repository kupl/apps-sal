import fractions
# import math as fractions
mod = 10**9 + 7
n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print((1))
    return

g = fractions.gcd(a[0], a[1])  # 最大公約数
f = a[0] * a[1] // g  # 最小公倍数
ans = a[0] // g + a[1] // g

for i in range(2, n):
    # print(ans, g, f)
    h = fractions.gcd(f, a[i])
    g = a[i] // h
    f = f * a[i] // h
    ans *= g
    ans += f // a[i]
    ans %= mod
print((ans % mod))
