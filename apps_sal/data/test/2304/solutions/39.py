def root(x):
    if(par[x]==x):
        return x
    else:
        r=root(par[x])
        diff_weight[x]+=diff_weight[par[x]]
        par[x]=r
        return r

def weight(x):
    root(x)
    return diff_weight[x]

def diff(x,y):
    return weight(y)-weight(x)

def relate(a,b,w):
    w+=weight(a);w-=weight(b)
    a=root(a)
    b=root(b)
    if(a==b):
        return False
    if rank[a]<rank[b]:
        a,b=b,a
        w=-w
    if rank[a]==rank[b]:
        rank[b]+=1
        par[b]=a
    par[b]=a
    diff_weight[b]=w
    siz[a]+=siz[b]
    return True

def size(a):
    return siz[root(a)]
    
def same(a,b):
    return root(a)==root(b)
    
N,M=map(int,input().split())
par=[i for i in range(N)]
siz=[1 for _ in range(N)]
rank=[0 for _ in range(N)]
diff_weight=[0 for _ in range(N)]

for i in range(M):
    L,R,D=map(int,input().split())
    L,R=L-1,R-1
    if same(L,R) and diff(L,R)!=D:
        print('No')
        return
    else:
        relate(L,R,D)
print('Yes')
