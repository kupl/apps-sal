
INF = 10 ** 9

que = [0] * 1024


def bfs(g, flow, parent, s1, s2, t1, t2):

    qf = 0
    que[0] = s1
    que[1] = s2
    ql = 2

    while qf < ql:
        u = que[qf]
        qf += 1
        for v in g[u]:
            if 0 <= flow[u][v] and parent[v] == -1:
                parent[v] = u
                if v != t1 and v != t2:
                    que[ql] = v
                    ql += 1
                else:
                    return 1, v

    return 0, 0


def solve(h, w, g, s, t):

    n = h + w
    si, sj = s
    ti, tj = t

    if si == ti or sj == tj:
        return -1

    f = 0
    flow = [[0] * n for _ in range(n)]

    while True:
        parent = [-1] * n
        parent[si] = -2
        parent[sj] = -2

        m, te = bfs(g, flow, parent, si, sj, ti, tj)
        if m == 0:
            break
        f += 1
        v = te
        while v != si and v != sj:
            u = parent[v]
            flow[u][v] -= 1
            flow[v][u] += 1
            v = u

    return f


def main():
    h, w = input().split()
    h = int(h)
    w = int(w)
    g = [[] for _ in range(h + w)]
    s = None
    t = None
    for i in range(h):
        a = input()
        for j in range(w):
            ch = a[j]
            if ch == 'o':
                g[i].append(h + j)
                g[h + j].append(i)
            elif ch == 'S':
                s = (i, h + j)
            elif ch == 'T':
                t = (i, h + j)

    print((solve(h, w, g, s, t)))


def __starting_point():
    main()


__starting_point()
