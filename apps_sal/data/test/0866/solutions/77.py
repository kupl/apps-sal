mod=int(1e9)+7
f=[1]
for i in range(1,int(1e6)):f.append(i*f[i-1]%mod)
def comb(a,b):
    return f[a]%mod*pow(f[b],mod-2,mod)%mod*pow(f[a-b],mod-2,mod)%mod
x,y=map(int,input().split())
if (2*y-x)%3 or (2*x-y)%3:
    print(0)
    return
else:
    a,b=(2*y-x)//3,(2*x-y)//3
    if not(a>=0 and b>=0):
        print(0)
        return
    print(comb(a+b,b))
