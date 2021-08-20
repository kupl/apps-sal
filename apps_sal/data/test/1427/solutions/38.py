import math
n = int(input())
a = list(map(int, input().split()))


def lcm(a, b):
    return a * b // math.gcd(a, b)


p = 1000000007
k = 1
for i in range(n):
    k = lcm(k, a[i])
k %= p
ans = 0
for i in range(n):
    ans += k * pow(a[i], p - 2, p)
    ans %= p
print(ans)
