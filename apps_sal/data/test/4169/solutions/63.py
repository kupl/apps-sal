N,M=map(int,input().split())
L=sorted([tuple(map(int,input().split())) for i in range(N)])
ans=0
for a,b in L:
    if M>b:
        ans+=a*b
        M-=b
    else:
        ans+=a*M
        break
print(ans)
