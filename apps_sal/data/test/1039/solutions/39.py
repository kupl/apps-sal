N=int(input())
G=[[] for _ in range(N)]
for i in range(N-1):
    a,b,c=list(map(int,input().split()))
    G[a-1].append([b-1,c])
    G[b-1].append([a-1,c])

Q,K=list(map(int,input().split()))

SD=[0]*N
seen=[0]*N
stack=[]
stack.append([K-1,0])
seen[K-1]=1
while stack:
    x,d=stack.pop()
    for y,d0 in G[x]:
        if seen[y]==0:
            SD[y]=d+d0
            stack.append([y,d+d0])
            seen[y]=1
for i in range(Q):
    x,y=list(map(int,input().split()))
    ans=SD[x-1]+SD[y-1]
    print(ans)


