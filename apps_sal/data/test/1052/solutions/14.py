import math
def der(n):
    sm=0
    p=1
    for i in range(0,n+1):
        sm+=p*(math.factorial(n)//math.factorial(i))
        p=p*(-1)
    return sm
def nCr(n,r):
    f=math.factorial
    return (f(n)//(f(r)*f(n-r)))
n,k=(int(i) for i in input().split())
ans=0
for i in range(0,k+1):
    ans+=(nCr(n,i)*der(i))
print(ans)
    

