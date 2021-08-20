"""
n,m = map(int,input().split())
eg,deg = [[] for _ in range(n+1)],[0 for _ in range(n+1)]
f,rk = list(range(n+1)),[0 for _ in range(n+1)]
def fd(a):
    if f[a]!=a :return fd(f[a]) 
    return f[a]
def un(a,b):
    ra,rb = fd(a),fd(b)
    if ra==rb:return 
    if rk[ra]>=rk[rb]:
        f[rb] = ra
        if rk[ra]==rk[rb]:rk[ra] +=1
    else :f[ra] = rb
for i in range(1,n+1):
    for j in eg[i]:
        un(j,i)
for x,y in [map(int,input().split()) for _ in range(m)]:
    un(x,y)
    deg[x],deg[y] = deg[x]+1,deg[y]+1
table = [0 for _ in range(n+1)]
for i in range(1,n+1):
    table[f[i]] += 1
ok = 1
for i in range(1,n+1):
    if deg[i]!=table[f[i]]-1:
        ok = 0
        break
print("YES") if ok else print("NO")
"""
(n, m) = [int(x) for x in input().split()]
d = {}
visited = set()
for x in range(m):
    (a, b) = input().split()
    d.setdefault(a, {a}).add(b)
    d.setdefault(b, {b}).add(a)
res = 'YES'
for (x, y) in d.items():
    if x not in visited:
        if all([d[u] == y for u in y]):
            visited.update(y)
        else:
            res = 'NO'
            break
print(res)
