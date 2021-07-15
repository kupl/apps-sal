# solution
import io

nim,mike=map(int,input().split())

abc=[list(map(int,input().split())) for _ in [0]*mike]

g=[[] for _ in [0]*nim]
[g[a-1].append([b-1,c]) for a,b,c in abc]

dist=[-10**15 for _ in [0]*nim]
dist[0]=0
a,b=-10**15,-10**15

for _ in range(nim):
    for p in range(nim):
        for i,j in g[p]:
            dist[i]=max(dist[i],dist[p]+j)
    a,b=b,dist[nim-1]

if a==b:
    print(a)
else:
    print("inf")
