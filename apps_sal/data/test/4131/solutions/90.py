import bisect
(N, M) = map(int, input().split())
d = {}
PY = []
for _ in range(M):
    (p, y) = map(int, input().split())
    PY.append((p, y))
    t = d.get(p, [0])
    i = bisect.bisect_left(t, y)
    t.insert(i, y)
    d[p] = t
dx = {}
for (k, v) in d.items():
    for i in range(len(v)):
        dx[k, v[i]] = i
for (p, y) in PY:
    print(str(p).zfill(6) + str(dx[p, y]).zfill(6))
