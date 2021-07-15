n=int(input())
a=list(map(int,input().split()))
l=0
r=n-1
b=[0,0]
for i in range(n):
    if a[l]>a[r]:
        b[i%2]+=a[l]
        l+=1
    else:
        b[i%2]+=a[r]
        r-=1
print(b[0],b[1])
