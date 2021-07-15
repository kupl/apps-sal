n,m=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]
arr.append(1000000002)
arr=sorted(arr)
curr=0
i=1
res=[]
ans=0
while m>=i:
    if i==arr[curr]:
        i+=1
        curr+=1
        continue
    ans+=1
    res.append(i)
    m-=i
    i+=1
print(ans)
for x in res:
    print(x,end=' ')
