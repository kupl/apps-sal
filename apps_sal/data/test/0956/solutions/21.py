xs = dict()
all = set()

n, k = list(map(int, input().split()))

for i in range(n):
    a, b = list(map(int, input().split()))
    try:
        xs[a].add(b)
    except KeyError:
        xs[a] = {b}
    try:
        xs[b].add(a)
    except KeyError:
        xs[b] = {a}
    all.add(a)
    all.add(b)

ys = dict()

for x in xs:
    n = len(xs[x])
    r = []
    for y in all - xs[x] - {x}:
        h = len(xs[x] & xs[y])
        if 100 * h >= n * k:
            r.append(y)
    ys[x] = r

for y in sorted(list(ys.items()), key=lambda p: p[0]):
    print('{}: {} {}'.format(y[0], len(y[1]), ' '.join(list(map(str, sorted(y[1]))))))


