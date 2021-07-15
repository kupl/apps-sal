n,m=map(int,input().split(' '))
piece=[0]*m
for i in range(m):
    piece[i]=tuple(map(int,input().split(' ')))

node=[0]+[float('inf')]*(n-1)

for v in range(n-1):
    for e in range(m):
        a,b,c=piece[e]
        if node[b-1] > node[a-1]-c:
            node[b-1] = node[a-1]-c
ans=node[n-1]
for e in range(m):
    a,b,c=piece[e]
    if node[b-1] > node[a-1] - c:
        node[b-1] = node[a-1] -c

if ans != node[n-1]:
    print('inf')
else:
    print(-ans)
