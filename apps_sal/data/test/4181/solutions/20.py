n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

c=0

for i in range(n):
    if a[i]<b[i]:
        c+=min(a[i]+a[i+1],b[i])
        a[i+1]=max(a[i+1]+a[i]-b[i],0)        
    else:
        c+=b[i]

print(c)
