n=int(input())
a=sorted(map(int,input().split()))
left,right=0,0
ans=1
while right<n-1:
    if a[right+1]-a[left]<=5:
        right+=1
        ans=max(ans,right-left+1)
    elif left<right:
        left+=1
    else:
        left+=1
        right+=1
print(ans)
