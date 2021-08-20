INF = 10000000000.0
(n, s, k) = list(map(int, input().split()))
r = list(map(int, input().split()))
r.append(0)
col = input()
mat = []
for i in range(n + 1):
    adj = {}
    for j in range(n):
        if i == n:
            adj[j] = abs(s - 1 - j)
        elif col[i] != col[j] and r[i] < r[j]:
            adj[j] = abs(i - j)
    mat.append(adj)
mem = [{} for i in range(n + 1)]


def get(s, k):
    if mem[s].get(k):
        return mem[s].get(k)
    if r[s] >= k:
        mem[s][k] = 0
    else:
        mi = None
        for nei in mat[s]:
            ncost = get(nei, k - r[s])
            if ncost is None:
                continue
            curr = ncost + mat[s][nei]
            if mi is None or curr < mi:
                mi = curr
        if mi is not None:
            mem[s][k] = mi
        else:
            mem[s][k] = INF
    return mem[s].get(k)


ans = get(n, k)
if ans is None or ans >= INF:
    print(-1)
else:
    print(ans)
