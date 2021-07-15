def find(fa, x) : 
    if fa[x] == x :
        return x
    else :
        fa[x] = find(fa, fa[x])
        return fa[x]
n, m = list(map(int, input().split()))
fa = []
for i in range(n) :
    fa.append(i)
ans = 1
for i in range(m) :
    x, y = [int(x) - 1 for x in input().split()]
    if find(fa, x) != find(fa, y) :
        ans *= 2
        fa[find(fa, x)] = fa[y]
print(ans)


