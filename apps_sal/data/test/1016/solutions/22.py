n, m = map(int, input().split())
e = [[] for x in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    e[x].append(y)
    e[y].append(x)
c = set(range(1, n + 1))
val = 2 ** n
while c:
    s = c.pop()
    dfs = [s]
    val //= 2
    while dfs:
        cur = dfs.pop()
        for nxt in e[cur]:
            if nxt in c:
                dfs.append(nxt)
                c.remove(nxt)
print(val)
