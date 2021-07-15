n,x=list(map(int,input().split()))
a=list(map(int,input().split()))
s=0
for i in range(1,n):
    b=a[i-1]+a[i]-x
    if b>0:
        s+=b
        a[i]=max(a[i]-b,0)
print(s)

