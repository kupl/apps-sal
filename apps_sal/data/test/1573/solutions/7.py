n,d=map(int, input().split())
arr=[]
for i in range(n):
    arr.append(tuple(map(int, input().split())))
arr=sorted(arr)
prefix=[]
prefix.append(arr[0][1])
for i in range(1,n):
    prefix.append(prefix[i-1]+arr[i][1])
ans=0
for i in range(n):
    low=0
    high=n-1
    while low<high:
        mid=(low+high+1)//2
        if arr[mid][0]>=arr[i][0]+d:
            high=mid-1
        else:
            low=mid
    if i==0:
        ans=prefix[low]
    elif prefix[low]-prefix[i-1]>ans:
        ans=prefix[low]-prefix[i-1]
print(ans)
