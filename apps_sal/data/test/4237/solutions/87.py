import math


def lcm(a):
    LCM = a[0]
    for i in range(1, len(a)):
        LCM = LCM * a[i] // math.gcd(LCM, a[i])
    return LCM


def f(k):
    return b // k - (a - 1) // k


(a, b, c, d) = map(int, input().split())
ALL = b - a + 1
ans = ALL - (f(c) + f(d) - f(lcm([c, d])))
print(ans)
