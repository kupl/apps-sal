n,m=list(map(int,input().split()))
a=list(map(int,input().split()))
b=1
s=0
for i in range(0,m):
    if b>a[i]:
        s+=a[i]+n-b
    else:
        s+=a[i]-b
    b=a[i]
print(s)
