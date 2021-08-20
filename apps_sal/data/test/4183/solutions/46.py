import math
N = int(input())


def lcm(x, y):
    return x * y // math.gcd(x, y)


ans = 1
for _ in range(N):
    T = int(input())
    ans = lcm(ans, T)
print(ans)
