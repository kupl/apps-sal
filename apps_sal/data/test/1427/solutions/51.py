def gcd(a, b):
    if b==0:
        return a
    return gcd(b, a%b)

def lcm(a, b):
    return a*(b//gcd(a, b))

mod = int(1e9+7)
def ext_gcd(a, b, x, y):
    if b==0:
        x[0] = 1
        y[0] = 0
        return a
    g = ext_gcd(b, a%b, y, x)
    y[0]-=a//b*x[0]
    return g

def mod_inv(a):
    x = [0]
    y = [0]
    ext_gcd(a, mod, x, y)
    return (x[0]%mod + mod)%mod;

n = int(input())
vs = list(map(int, input().split()))
l = 1
for x in vs:
    l = lcm(l, x)
l = l%mod;
ans = 0
for x in vs:
    ans = (ans + ((l*mod_inv(x))%mod))%mod
print(ans)

