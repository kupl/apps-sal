from math import gcd


def lcm(a, b):
    return (a * b) // gcd(a, b)


N = int(input())
ans = 1
for i in range(2, N + 1):
    ans = lcm(ans, i)
ans = 2 * ans + 1
print(ans)
