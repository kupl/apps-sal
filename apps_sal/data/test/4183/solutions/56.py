n = int(input())
t = [int(input()) for _ in range(n)]

import math

def lcm(x,y):
    return (x * y) // math.gcd(x, y)

ans = 1
for i in range(n):
    ans = lcm(ans,t[i])
print(ans)
