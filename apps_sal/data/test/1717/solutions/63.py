import math

n = int(input())


def fun(x, y):
    return (x * y) // math.gcd(x, y)


ans = 1
for i in range(1, n + 1):
    ans = fun(ans, i)

print(ans + 1)
