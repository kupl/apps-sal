#Union Find

#xの根を求める
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
#xとyの属する集合の併合
def unite(x,y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return False
    else:
        #sizeの大きいほうがx
        if par[x] > par[y]:
            x,y = y,x
        par[x] += par[y]
        par[y] = x
        return True

#xとyが同じ集合に属するかの判定
def same(x,y):
    return find(x) == find(y)

#xが属する集合の個数
def size(x):
    return -par[find(x)]

n,m=list(map(int,input().split()))
edge=[]
for _ in range(m):
    a,b=list(map(int,input().split()))
    a,b=a-1,b-1

    edge.append([a,b])


ans=0
for j in range(m):
    #初期化 
    #根なら-size,子なら親の頂点
    par = [-1]*n
    cnt=0
    for p in range(m):
        if p==j:
            continue
    
        e=edge[p]
        unite(e[0],e[1])  
          
    for k in range(n):
        if par[k]<0:
            cnt+=1

    if cnt>=2:
        ans+=1
    
    

    


print(ans)


