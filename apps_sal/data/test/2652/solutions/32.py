# xの根を求める
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
#xとyの属する集合の併合
def unite(x,y):
    x = find(x)
    y = find(y)

    if x == y:
        return False
    else:
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
n = int(input())
#初期化
#根なら-size,子なら親の頂点
par = [-1]*n

p = [] #点p
edge = []
for i in range(n):
    x,y = map(int,input().split())
    p.append([x,y,i])
p.sort(key=lambda x:x[0])
for i in range(n-1):
    x_0,_,j=p[i]
    x_1,_,k=p[i+1]
    edge.append([x_1-x_0,j,k]) # 重みx_1 - x_0の点jと点kを繋ぐ辺
p.sort(key=lambda x:x[1])
for i in range(n-1):
    _,y_0,j=p[i]
    _,y_1,k=p[i+1]
    edge.append([y_1-y_0,j,k])

edge.sort() #クラスカル法を使うので重みでソート
ans = 0
for i in range(len(edge)):
    cost,u,v = edge[i]
    if not same(u,v):
        unite(u,v)
        ans+=cost
print(ans)
