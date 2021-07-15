n,m=[int(x) for x in input().split()]
link=[0]*(n+1)
size=[0]*(n+1)
arr=[0]*m
res=0
for i in range(1,n+1):
    link[i]=i
    size[i]=1
def find(x):
    while x!=link[x]:
        x=link[x]
    return x
def comb(n):
    return n*(n-1)//2
def unite(a,b,res):
    a=find(a)
    b=find(b)
    if size[a]<size[b]:
        a,b=b,a
    res=res-comb(size[a])-comb(size[b])+comb(size[a]+size[b])
    size[a]+=size[b]
    link[b]=a
    return res
edges=[]
ask=[]
for i in range(n-1):
    x,y,z=[int(x) for x in input().split()]
    edges.append((z,x,y))
edges.sort()
x=0
edges.append((10**100,1,1))
ask=sorted(zip([int(x) for x in input().split()],list(range(m))))
for i in range(m):
    while edges[x][0]<=ask[i][0]:
        res=unite(edges[x][1],edges[x][2],res)
        x+=1
    arr[ask[i][1]]=res
print(*arr)
    

