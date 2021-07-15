#Union Find

#xの根を求める
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

N, M = map(int, input().split())
bridges = []

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    bridges.append((a, b))

#初期化
#根なら-size,子なら親の頂点
par = [-1]*N
tot = N*(N-1)//2
ans = [tot]

for a, b in bridges[::-1]:
    if not same(a, b): 
        tot -= size(a)*size(b)
    unite(a, b)
    ans.append(tot)

print('\n'.join(map(str, ans[:-1][::-1])))
