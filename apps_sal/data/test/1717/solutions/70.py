import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

n = int(input())
ans = 1
for i in range(2, n+1):
    ans = lcm(ans, i)
print(ans + 1)
