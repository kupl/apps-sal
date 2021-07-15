N,M=map(int,input().split())
ans=0
if M>=2*N:
    ans+=N
else:
    ans+=M//2
    print(ans)
    return

M-=2*N
ans+=M//4
print(ans)
