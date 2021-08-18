from itertools import chain
with open(0) as f:
    N, *xy = map(int, f.read().split())

from collections import namedtuple
v = namedtuple('v', ['coordinate', 'num'])
X = sorted([v(x, i) for x, i in zip(xy[::2], range(N))])
Y = sorted([v(y, i) for y, i in zip(xy[1::2], range(N))])


def diffiter(X): return zip(X[:len(X) - 1], X[1:])
def cost(u, v): return abs(u.coordinate - v.coordinate)


Edge = sorted([(cost(u, v), u.num, v.num) for u, v in chain(diffiter(X), diffiter(Y))])

root = namedtuple('root', ['num', 'rank'])
Root = [root(i, 0) for i in range(N)]


def fr(i):
    if i == Root[i].num:
        return Root[i]
    Root[i] = fr(Root[i].num)
    return Root[i]


def unionT(i, j):
    p, q = fr(i), fr(j)
    if p.rank < q.rank:
        Root[p.num] = q
    elif p.rank > q.rank:
        Root[q.num] = p
    elif p.rank == q.rank:
        r, s = min(p, q), max(p, q)
        Root[r.num] = Root[s.num] = root(r.num, r.rank + 1)


ans = 0
for w, i, j in Edge:
    if fr(i).num == fr(j).num:
        continue
    else:
        unionT(i, j)
        ans += w
print(ans)
