N=int(input())
ans=0
for _ in range(N-1):
    u,v=map(int,input().split())
    u,v=min(u-1,v-1),max(u-1,v-1)
    ans-=(u+1)*(N-v)
for i in range(1,N+1):
    ans+=i*(i+1)//2
print(ans)
