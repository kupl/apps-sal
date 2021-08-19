#  --*-coding:utf-8-*--

def dsMakeSet(ds, x):
    ds[x] = x


def dsFind(ds, x):
    if ds[x] == x:
        return x

    x0 = x
    while ds[x] != x:
        x = ds[x]

    ds[x0] = x
    return x


def dsUnion(ds, x, y):
    xRoot = dsFind(ds, x)
    yRoot = dsFind(ds, y)

    if xRoot != yRoot:
        ds[yRoot] = xRoot
        return True

    return False


N = int(input())
Q = {}

for _ in range(N):
    x, y = list(map(int, input().split()))

    X = ('x', x)
    Y = ('y', y)

    if not (X in Q):
        dsMakeSet(Q, X)

    if not (Y in Q):
        dsMakeSet(Q, ('y', y))

    dsUnion(Q, X, Y)

R = {}

for q in Q:
    root = dsFind(Q, q)

    if not(root in R):
        R[root] = [0, 0]

    r = R[root]
    if q[0] == 'x':
        r[0] += 1
    else:
        r[1] += 1

s = 0
for r in list(R.values()):
    s += r[0] * r[1]

print((s - N))
