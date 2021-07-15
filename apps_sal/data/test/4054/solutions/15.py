a=list(map(int,input().split()))
ans=100
ans=min(ans,a[0])
ans=min(ans,a[1])
ans=min(ans,a[2]//2)
ans=min(ans,a[3]//7)
ans=min(ans,a[4]//4)
print(ans)
