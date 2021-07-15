import math


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


MOD = 1000000007

N = int(input())

A = list(map(int, input().split()))

lcm_ = 1
for a in A:
    lcm_ = lcm(lcm_, a)

ans = 0
for a in A:
    ans += lcm_ // a

ans %= MOD
print(ans)
