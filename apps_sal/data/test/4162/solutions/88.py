n = int(input())
a = list(map(int, input().split()))

import math

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

l = 1
for i in range(n):
    l = lcm(l, a[i])

ans = 0
for i in range(n):
    ans += (l - 1) % a[i]

print(ans)
