n = int(input().strip())
vlrs = [tuple(map(int, input().strip().split())) for _ in range(n)]
vlrs = [(v, l - (0 if l < 0 else 1), r - (0 if r < 0 else 1)) for (v, l, r) in vlrs]
isroot = [True for _ in range(n)]
for (v, l, r) in vlrs:
    if l != -1:
        isroot[l] = False
    if r != -1:
        isroot[r] = False
root = isroot.index(True)
vs = [v for (v, l, r) in vlrs]
vmin = min(vs)
vmax = max(vs)
found = set()


def DFS(U, vl, vr):
    while vlrs[U].count(-1) == 1:
        (v, L, R) = vlrs[U]
        if vl <= v <= vr:
            found.add(v)
        if L != -1:
            (U, vl, vr) = (L, vl, min(v, vr))
        else:
            (U, vl, vr) = (R, max(v, vl), vr)
    (v, L, R) = vlrs[U]
    if vl <= v <= vr:
        found.add(v)
    if L != -1 and R != -1:
        DFS(L, vl, min(v, vr))
        DFS(R, max(v, vl), vr)


DFS(root, vmin, vmax)
res = sum((1 for v in vs if v not in found))
print(res)
