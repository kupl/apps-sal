from functools import reduce
n = int(input())
(a, b) = (list(map(int, input().split())) for _ in (None, None))
oq = set(range(4))
q = oq.copy()
w = []
possible = True
for i in range(n - 1):
    p = set()
    w.append({})
    for t1 in q:
        e = set([t2 for t2 in oq if t2 | t1 == a[i] and t2 & t1 == b[i]])
        p |= e
        w[i][t1] = e
    q = p
    if len(q) == 0:
        possible = False
        break
print('YES' if possible else 'NO')
if possible:
    y = None
    for l in q:
        y = l
        break
    path = [y]
    for g in reversed(w):
        for (k, u) in list(g.items()):
            if y in u:
                y = k
                break
        path.append(y)
    print(reduce(lambda x, y: x + ' ' + str(y), reversed(path), '')[1:])
