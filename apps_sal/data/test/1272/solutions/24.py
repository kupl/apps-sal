import sys
input = sys.stdin.readline

n,m = map(int,input().split())
edge = [tuple(map(int,input().split())) for i in range(m)]
#辺を足していくので逆順で考える
edge = edge[::-1]

par = [i for i in range(n+1)]
rank = [1] * (n+1)
size = [1] * (n+1)

###Union-Find
def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def same_check(x, y):
        return find(x) == find(y)

    #併合(Union)
def union(x, y):
    #根を探す
    x = find(x)
    y = find(y)

    #木の高さを比較し、低いほうから高いほうに根を張る
    if rank[x] < rank[y]:
        par[x] = y
        size[y] += size[x]
    else:
        par[y] = x
        size[x] += size[y]
        if rank[x] == rank[y]:
            rank[x] += 1

result = []
for i in range(m):
    a = find(edge[i][0])
    b = find(edge[i][1])
    if a == b:
        result.append(0)
    else:
        result.append(size[a]*size[b])
        union(a,b)

ans = 0
for i in range(m):
    ans += result[m-i-1]
    print(ans)
