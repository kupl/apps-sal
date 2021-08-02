import math


def lcm(a, b):
    return a * b // math.gcd(a, b)


N = int(input())
T = [int(input()) for _ in range(N)]
ans = 1
for t in T:
    ans = lcm(ans, t)
print(ans)
