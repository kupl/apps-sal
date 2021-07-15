def merge(l,r):
    nonlocal num
    if l>=r:
        return 
    mid=(l+r)>>1
    merge(l,mid)
    merge(mid+1,r)
    j=mid+1
    for i in range(l,mid+1):
        while j<=r and arr[j]-arr[i]<t:
            j+=1
        num+=j-mid-1
    arr[l:r+1]=sorted(arr[l:r+1])
n,t=map(int,input().split())
List=list(map(int,input().split()))
num=0
arr=[0]*(n+1)
for i in range(1,n+1):
    arr[i]=arr[i-1]+List[i-1]
merge(0,n)
print(num)
