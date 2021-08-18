import sys

stdin = sys.stdin


def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))
def ns(): return stdin.readline().rstrip()


n, m = na()
g = [[False] * n for _ in range(n)]
gs = [[] for _ in range(n)]
for i in range(m):
    s, t = na()
    gs[s - 1].append(t - 1)
    g[s - 1][t - 1] = True

ans = 999999
best = None
for i in range(n):
    ds = [9999999] * n
    prevs = [-1] * n
    ds[i] = 0
    q = [i]
    qp = 0
    while qp < len(q):
        cur = q[qp]
        qp += 1
        for e in gs[cur]:
            if ds[e] > ds[cur] + 1:
                ds[e] = ds[cur] + 1
                prevs[e] = cur
                q.append(e)
    for j in range(n):
        if g[j][i]:
            if ds[j] + 1 < ans:
                ans = ds[j] + 1
                best = [0] * (ds[j] + 1)
                best[0] = i
                cur = j
                r = -1
                while cur != i:
                    best[r] = cur
                    r -= 1
                    cur = prevs[cur]

if not best:
    print((-1))
else:
    print(ans)
    for x in best:
        print((x + 1))
