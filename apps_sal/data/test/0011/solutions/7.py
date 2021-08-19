from fractions import gcd


def lcm(x, y):
    return x * y // gcd(x, y)


(n, a, b, p, q) = list(map(int, input().split()))
ans = p * (n // a)
ans += q * (n // b)
ans -= min(p, q) * (n // lcm(a, b))
print(ans)
