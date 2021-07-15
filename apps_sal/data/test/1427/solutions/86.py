import math

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

n = int(input())
a = list(map(int,input().split()))
mod = 10**9 + 7

lc = 1
for i in range(n):
    lc = lcm(lc,a[i])
ans = 0
for i in range(n):
    ans += lc * pow(a[i],-1,mod)
    ans %= mod
print(ans)
