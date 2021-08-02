import math
n = int(input())


def lcm(x, y):
    return x * y // math.gcd(x, y)


ans = 1
for i in range(1, n + 1):
    ans = lcm(i, ans)
print((ans + 1))
