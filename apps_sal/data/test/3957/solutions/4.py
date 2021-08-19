from collections import defaultdict


def put():
    return map(int, input().split())


def dfs():
    s = [(1, 0)]
    ans = 0
    vis = [0] * (n + 1)
    while s:
        (i, p) = s.pop()
        if vis[i] == 0:
            vis[i] = 1
            s.append((i, p))
            for j in tree[i]:
                if j != p:
                    s.append((j, i))
        elif vis[i] == 1:
            vis[i] = 2
            for j in tree[i]:
                if j != p:
                    mark[i] += mark[j]
            ans += min(mark[i], 2 * k - mark[i])
    print(ans)


(n, k) = put()
l = list(put())
edge = defaultdict()
tree = [[] for i in range(n + 1)]
mark = [0] * (n + 1)
for i in l:
    mark[i] = 1
for _ in range(n - 1):
    (x, y) = put()
    tree[x].append(y)
    tree[y].append(x)
dfs()
