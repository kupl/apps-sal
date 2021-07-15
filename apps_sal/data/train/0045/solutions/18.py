arr=[]
s=1
i=1
while s<((10**18)+1):
    temp=(s*(s+1))//2
    arr.append(temp)
    s+=(2**i)
    i+=1
t=int(input())
for i in range(t):
    x=int(input())
    ans=0
    j=0
    while x>0:
        if arr[j]<=x:
            x-=arr[j]
            ans+=1
        else:
            x=0
        j+=1
    print(ans)
