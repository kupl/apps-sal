from collections import defaultdict
(N, M) = map(int, input().split())
PY = [list(map(int, input().split())) for _ in range(M)]
di = defaultdict(list)
for (i, py) in enumerate(PY):
    di[py[0]].append([py[1], i])
ans = ['' for _ in range(M)]
for (k, v) in di.items():
    v.sort()
    for (j, yi) in enumerate(v):
        s = str(k).zfill(6)
        t = str(j + 1).zfill(6)
        ans[yi[1]] = s + t
print('\n'.join(ans))
