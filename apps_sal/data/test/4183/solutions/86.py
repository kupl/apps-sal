import math
n = int(input())
T = [int(input()) for _ in range(n)]


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


ans = T[0]
for t in T[1:]:
    ans = lcm(ans, t)
print(ans)
