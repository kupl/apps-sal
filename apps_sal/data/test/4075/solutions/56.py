N,M=map(int,input().split())
k=[]
s=[]
for i in range(M):
    ks=list(map(int,input().split()))
    k.append(ks[0])
    s.append(list(map(lambda x:x-1,ks[1:])))
p=list(map(int,input().split()))

ans=0
for i in range(2**N):
    isOK=True

    for j in range(M):
        sum=0
        for x in s[j]:
            sum+=(i>>x)&1
        
        if sum%2!=p[j]:
            isOK=False
    
    if isOK:
        ans+=1

print(ans)
