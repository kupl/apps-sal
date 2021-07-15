x, y = map(int, input().split())
mod = 10**9+7

if (2*y-x < 0) or (2*x-y < 0):
    print(0)
    return

if (2*y-x)%3 != 0 or (2*x-y)%3 != 0:
    print(0)
    return

xc = (2*y-x)//3
yc = (2*x-y)//3
p = 1
k = 1
for i in range(1, xc+1):
    p *= (yc+i)
    k *= i
    p %= mod
    k %= mod

ans = p*pow(k, mod-2, mod)%mod
print(ans)
