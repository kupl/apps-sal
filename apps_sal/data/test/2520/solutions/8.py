N,M,K=map(int,input().split())
par=[-1]*N
def find(x):
    if par[x] < 0:
        return x
    else:
        tank = []
        while par[x] >= 0:
            tank.append(x)
            x = par[x]
        for elt in tank:
            par[elt] = x
        return x
def unite(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    else:
      if find(x)>find(y):x,y=y,x
      par[x] += par[y]
      par[y] = x
      return True
frbl=[0]*N
for i in range(M):
  a,b=sorted(map(int,input().split()))
  unite(a-1,b-1)
  frbl[a-1]+=1;frbl[b-1]+=1
block=[0]*N
for i in range(K):
  c,d=sorted(map(int,input().split()))
  if find(c-1)==find(d-1):
    frbl[c-1]+=1;frbl[d-1]+=1
list=[]
for i in range(N):
  list.append(max(-par[find(i)]-frbl[i]-1,0))
print(*list)
