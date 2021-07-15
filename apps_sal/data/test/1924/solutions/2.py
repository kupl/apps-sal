mod = 10**9+7

f = [1]*(2*10**6+5)
f[0] = 1
for i in range(1,2*10**6+4):
    f[i] = f[i-1]*i%mod

def inv(i):
    return pow(f[i],mod-2,mod)

def g(x,y):
    return f[x+y]*inv(x)*inv(y)%mod

r1,c1,r2,c2 = map(int,input().split(" "))
ans = g(r2+1,c2+1)-g(r2+1,c1)-g(r1,c2+1)+g(r1,c1)
print(ans%mod)
