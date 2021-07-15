(n,k)=list(map(int, input().split()))
a=list(map(int, input().split()))
ans=0
for i in range(n):
    if 5-a[i]>=k:
        ans+=1   
print(ans//3)

