n,k=list(map(int,input().split()))

L=input().split()
ans=0
for i in range(n):
    x=0
    for item in L[i]:
        if(item=='4' or item=='7'):
            x+=1
    if(x<=k):
        ans+=1
print(ans)

