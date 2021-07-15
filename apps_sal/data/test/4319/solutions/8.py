n=int(input())
arr=list(map(int,input().split()))
arr2=[]
ans=1
for i in range(1,n):
    if(arr[i]==1):
        ans+=1
        arr2.append(arr[i-1])
arr2.append(arr[-1])
print(ans)
print(*arr2)
