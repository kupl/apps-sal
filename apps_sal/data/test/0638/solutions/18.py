n,m=list(map(int,input().split()))
l=[int(i) for i in input().split()]
pre=[0]*(n+1)
for i in range(1,n+1):
    pre[i]=pre[i-1]+l[i-1]
ans=[0]*n 
arr=[]
for i in range(n):
    if pre[i+1]<=m:
        ans[i]=0 
        arr.append(l[i])
    else:
        arr.sort()
        rem=m-l[i]
        c=0 
        sm=pre[i]
        j=len(arr)-1
        while sm>rem:
            sm-=arr[j]
            j-=1
            c+=1 
        ans[i]=c 
        arr.append(l[i])
print(*ans)
        
        

