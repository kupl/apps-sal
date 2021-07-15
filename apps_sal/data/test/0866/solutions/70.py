def inv(a,p):
    if a==1:
        return 1
    elif a==0:
        return 0
    return p-(inv(p%a,p)*(p//a))%p
x,y=map(int,input().split())
if (x+y)%3!=0:
    print("0")
    return
if x==0 and y>0:
    print("0")
    return
if y/x>2 or y/x<0.5:
    print("0")
    return
n=(x+y)//3
r=(2*x-y)//3
p=10**9+7
def fact(n,p):
    a=[[] for _ in range(n+1)]
    a[0]=1
    for i in range(n):
        a[i+1]=(a[i]*(i+1))%p
    return a
f=fact(n,p)
c=f[-1]
d=f[r]
e=f[n-r]
dd=inv(d,p)
ee=inv(e,p)
ans=(c*dd*ee)%p
print(ans)
