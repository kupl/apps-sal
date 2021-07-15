n,k=map(int,input().split())
a=list(map(int,input().split()))
ans=0
if n==1:
    if a[0]>=k:
        print(1)
        return
    else:
        print(0)
        return
right=0
sum=0
for left in range(n):
    while right<n and sum<k:
        sum+=a[right]
        right+=1
    if sum<k:
        break
    ans+=(n-right+1)
    if right==left:
        right+=1
    else:
        sum-=a[left]
print(ans)
