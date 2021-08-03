gr = {}


class node:
    def __init__(self):
        self.adj = set()

    def add(self, b):
        self.adj.add(b)


n, m, k = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    gr[i + 1] = node()
for i in range(m):
    u, v = map(int, input().split())
    gr[u].add(v)
    gr[v].add(u)
v = [False for i in range(n + 1)]
v[0] = True
ans = 0
maxi = 0
c = 0
for i in a:
    s = set([i])
    ed = 0
    ne = 0
    last = 0
    while s:
        x = s.pop()
        ed += len(gr[x].adj)
        ne += 1
        v[x] = True
        for j in gr[x].adj:
            if j == last or v[j]:
                continue
            s.add(j)
        last = x
    if maxi < ne:
        maxi = ne
        c = ed // 2
    ans += ne * (ne - 1) // 2 - ed // 2
b = v.count(False)
if b != 0:
    edge = 0
    for i in range(1, n + 1):
        if v[i]:
            continue
        s = set([i])
        ed = 0
        last = 0
        while s:
            x = s.pop()
            ed += len(gr[x].adj)
            v[x] = True
            for j in gr[x].adj:
                if j == last or v[j]:
                    continue
                s.add(j)
            last = x

        edge += ed // 2
    ans = ans - maxi * (maxi - 1) // 2 + (maxi + b) * (maxi + b - 1) // 2 - edge
print(ans)
