N,X,M=map(int,input().split())
table=[X]
visited=[-1]*M
visited[X]=1

ans=X

for i in range(N-1):
    nx=table[i]**2
    nx%=M
    if visited[nx]>0:
        first=table.index(nx)
        oneloop=i+1-first
        rest=N-i-1
        loops=rest//oneloop
        totalofoneloop=sum(table[first:])
        ans+=totalofoneloop*loops
        remain=rest%oneloop
        ans+=sum(table[first:first+remain])
        print(ans)
        return
    else:
        table.append(nx)
        visited[nx]=1
        ans+=nx
 

print(ans)
