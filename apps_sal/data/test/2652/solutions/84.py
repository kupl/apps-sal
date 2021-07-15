N=int(input())
A=[]
for i in range(N):
  x,y=map(int,input().split())
  A.append((x,y,i))
A=sorted(A)
B=sorted(A,reverse=False, key=lambda x: x[1]) 
#print(A,B)
E=[]
for i in range(N-1):
  E.append(((A[i+1][0]-A[i][0]),A[i][2],A[i+1][2]))
  E.append(((B[i+1][1]-B[i][1]),B[i][2],B[i+1][2]))
edge=E

def kruskal():
    cost=0
    edge.sort()
    for c,u,v in edge:
        if same(u,v):
            continue
        union(u,v)
        cost+=c
    return cost

def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    if par[x] > par[y]:
        x, y = y, x
    par[x] += par[y]
    par[y] = x
    return True

def same(x, y):
    return find(x) == find(y)
par=[-1]*N
print(kruskal())
