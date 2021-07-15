# cook your dish here
n=int(input())
arr=[]
for i in range(n):
    arr.append([int(i) for i in input().split()])
arr.sort()
ans=1
i=0
p=arr[0][0]
q=arr[0][1]
while(i<n-1):
    i+=1
    if(arr[i][0]<=q):
        q=min(q,arr[i][1])
    else:
        ans+=1 
        q=arr[i][1]
print(ans)

