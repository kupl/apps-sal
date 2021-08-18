import sys
sys.setrecursionlimit(1100)


def dfs1(u, pre):
    vis[u] = True
    now.append(u)
    for v in to[u]:
        if v != pre:
            dfs1(v, u)


def dfs2(u, pre):
    mxdist[u] = dist[u]
    for v in to[u]:
        if v != pre:
            dist[v] = dist[u] + 1
            dfs2(v, u)
            mxdist[u] = max(mxdist[u], mxdist[v])


try:
    lab = 1
    n, m = [int(x) for x in input().split()]
    to = [[] for i in range(n + 10)]
    dist = [0 for i in range(n + 10)]
    mxdist = [0 for i in range(n + 10)]

    lab = 2
    for i in range(m):
        u, v = [int(x) for x in input().split()]
        to[u].append(v)
        to[v].append(u)

    com = []
    vis = [False for i in range(n + 10)]
    for i in range(1, n + 1):
        if vis[i] == False:
            now = []
            dfs1(i, 0)
            com.append(now)

    lab = 3
    ct = []
    mx = 0
    for lis in com:
        tmp = []
        d = 0
        for root in lis:
            for u in lis:
                dist[u] = mxdist[u] = 0
            dfs2(root, 0)
            tmp.append((mxdist[root], root))
            d = max(d, sum(sorted([mxdist[u] for u in to[root]])[-2:]))
        mx = max(mx, d)
        for x in tmp:
            if x[0] == (d + 1) // 2:
                center = [x[1] for x in tmp if x[0] == (d + 1) // 2][0]
        ct.append(((d + 1) // 2, center))

    lab = 4
    ct.sort(reverse=True)
    ans = []
    for i in range(1, len(ct)):
        mx = max(mx, ct[i][0] + 1 + ct[0][0])
        if i > 1:
            mx = max(mx, ct[i][0] + 2 + ct[1][0])
        ans.append((ct[i][1], ct[0][1]))
    print(mx)
    for p in ans:
        print(*p)
except Exception as e:
    print('error after lable', lab, ', type =', e)
