n, m = (int(t) for t in input().split(' '))
def direction(c):
    if c == '=': return 0
    if c == '>': return 1
    return -1

mx = [[direction(c) for c in input()] for _ in range(n)]

index = 0
class DSet(object):
    def __init__(self, value):
        nonlocal index
        self.values = set([value])
        self.index = index
        index += 1
        self.edges_to = set()
        self.edges_from = set()

    def __len__(self):
        return len(self.values)
    def update(self, other_dset):
        self.values.update(other_dset.values)

    def add_edge_to(self, i):
        self.edges_to.add(i)

    def add_edge_from(self, i):
        self.edges_from.add(i)

    def remove_edge_from(self, i):
        self.edges_from.remove(i)

dsu = [DSet(i) for i in range(n+m)]

def union(v1, v2):
    if len(dsu[v1]) > len(dsu[v2]):
        d = dsu[v1]
        d.update(dsu[v2])
    else:
        d = dsu[v2]
        d.update(dsu[v1])

    dsu[v1] = dsu[v2] = d

for i in range(n):
    for j in range(m):
        if not mx[i][j]:
            union(i, n + j)

for i in range(n):
    for j in range(m):
        if mx[i][j] > 0:
            dsu[i].add_edge_from(dsu[n + j].index)
            dsu[n+j].add_edge_to(dsu[i].index)
        elif mx[i][j] < 0:
            dsu[n + j].add_edge_from(dsu[i].index)
            dsu[i].add_edge_to(dsu[n+j].index)

weights = [1] * (n+m)
dsu_by_index = { d.index: d for d in dsu }

while True:
    try:
        v = next(d for d in range(n+m) if not len(dsu[d].edges_from) and len(dsu[d].edges_to))
    except:
        break

    dsuv = dsu[v]
    for edge in dsu[v].edges_to:
        dsue = dsu_by_index[edge]
        dsue.remove_edge_from(dsuv.index)
        for value in dsue.values:
            weights[value] = weights[v] + 1

    dsu[v].edges_to.clear()

ok = all(not len(d.edges_from) and not len(d.edges_to) for d in dsu)
if ok:
    print('Yes')
    print(*weights[0:n])
    print(*weights[n:])
else:
    print('No')

