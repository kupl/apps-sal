[n, m] = list(map(int, input().strip().split()))
bis = [tuple(map(int, input().strip().split())) for _ in range(m)]
tos = [[] for _ in range(n)]
for (u, v) in bis:
    tos[u - 1].append(v - 1)
    tos[v - 1].append(u - 1)
cands = set((i for i in range(n) if len(tos[i]) == 2))
res = 0
while cands:
    v = cands.pop()
    (R, L) = tos[v]
    while L in cands:
        cands.remove(L)
        (V1, V2) = tos[L]
        if V1 in cands:
            L = V1
        elif V2 in cands:
            L = V2
        else:
            break
        if L == R:
            res += 1
print(res)
