from collections import*
(n,m),*c = [[*map(int,i.split())]for i in open(0)]
g = [[]for _ in range(n+1)]

for a,b in c:
    g[a]+=[b]
    g[b]+=[a]

q=deque([1])
r=[0]*(n+1)

while q:
    v=q.popleft()
    for i in g[v]:
        if r[i]==0:
            r[i]=v
            q.append(i)

print("Yes",*r[2:],sep="\n")

