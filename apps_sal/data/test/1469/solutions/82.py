L = int(input())
v = 1
edges = []
n = 2
cost = 1
while n <=L:
    edges.append((v,v+1,0))
    edges.append((v,v+1,cost))
    cost *=2
    v += 1
    n*=2
goal = v
n //=2
N = n
L-=N
while L>0:
    if L>=n:
        edges.append((v,goal,N))
        L-=n
        N+=n
    n //=2
    v-=1
print(goal,len(edges))
for e in edges:
    print(*e)
