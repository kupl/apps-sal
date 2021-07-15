n=int(input())
arr=list(map(int,input().split()))
ans=0
arr.sort()
for i in range(0,n,2):
    ans+=arr[i+1]-arr[i]
print(ans)
