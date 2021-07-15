n=int(input())
mx=0;
a=list(map(int,input().split()))
for i in range(n):
    sum=0
    for j in range(i,n) :
        sum^=a[j]
        mx=max(mx,sum)
print(mx)

