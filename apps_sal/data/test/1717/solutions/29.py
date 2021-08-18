from math import gcd


def lcm(a, b):
    return a * b // gcd(a, b)


N = int(input())
ans = 1
for i in range(1, N + 1):
    ans = lcm(ans, i)
print(2 * ans + 1)
