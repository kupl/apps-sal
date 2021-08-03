import math


def lcm(a, b):
    return a * b // math.gcd(a, b)


n = int(input())
a = list(map(int, input().split()))
ans = lcm(a[0], a[1])
for i in range(1, n):
    ans = lcm(ans, a[i])
m = 0
for i in a:
    m += (ans - 1) % i
print(m)
