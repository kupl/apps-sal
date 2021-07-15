N,M = list(map(int,input().split()))
edges=[list([int(x)-1 for x in input().split()]) for _ in range(M)]
S,T = [int(x)-1 for x in input().split()]

N3=N*3
adj=[set() for _ in range(N3)]

for a,b in edges:
    for i in range(3):
        start = a+N*i
        dst = b+N*(i+1)
        adj[start%N3].add(dst%N3)


Q=[S]
visited={S}
dist=[-1]*N3
dist[S]=0

while Q:
    tmp=[]
    for q in Q:
        for i in adj[q]:
            if i in visited:
                continue
            else:
                dist[i]=dist[q]+1
                visited.add(i)
                tmp.append(i)
    Q = tmp
print((dist[T] if dist[T]==-1 else dist[T]//3))


