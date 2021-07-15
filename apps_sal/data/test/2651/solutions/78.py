mod=1000000007
n,m=list(map(int,input().split()))
x=[int(i) for i in input().split()]
y=[int(i) for i in input().split()]

xc=0
for i in range(1,n):
    a=x[i]-x[i-1]
    if i<=((n)//2):
        l=i
    else:
        l=n-i
    xc+=a*(l*n-(l*l))
    xc=xc%mod

yc=0
for i in range(1,m):
    a=y[i]-y[i-1]
    if i<=((m)//2):
        l=i
    else:
        l=m-i
    yc+=a*(l*m-(l*l))
    yc=yc%mod
print(((xc*yc)%mod))

