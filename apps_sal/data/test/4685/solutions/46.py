a=list(map(int,input().split()))
k=int(input())
c=max(a[0],a[1],a[2])
b=a[0]+a[1]+a[2]
b=b-c
for i in range(0,k):
    c=c*2
print(b+c)    
