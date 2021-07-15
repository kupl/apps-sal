MOD = 10**9+7
x=int(input())+1
n=1
n2=1
fac=1
for i in range(1,2*x+1):
    fac = (fac*i)%MOD
    if i==x:
        n=fac
    if i==2*x:
        n2=fac
res=  (n2*pow(n,MOD-2,MOD)**2)%MOD-1

print(res)

