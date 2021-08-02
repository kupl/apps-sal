from math import *


def lcm(x, y):
    return (x * y) // gcd(x, y)


N = int(input())
T = [int(input()) for _ in range(N)]
ans = T[0]
for i in range(1, N):
    ans = lcm(ans, T[i])
print(ans)
