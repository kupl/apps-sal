def bellman_ford(s, n, G):
    d = [float('inf')] * n
    d[s] = 0
    for i in range(n):
        update = False
        for x, y, z in G:
            if d[y] > d[x] + z:
                d[y] = d[x] + z
                update = True
        if not update:
            break
        if i == n - 1:
            return None
    return d


def main():
    n, m, p = map(int, input().split())
    G = []
    U = [[] for _ in range(n)]
    V = [[] for _ in range(n)]
    dic = {}
    for _ in range(m):
        a, b, c = map(int, input().split())
        if (a - 1, b - 1) in dic:
            if dic[(a - 1, b - 1)] > -c + p:
                dic[(a - 1, b - 1)] = -c + p
        else:
            dic[(a - 1, b - 1)] = -c + p
    for v in dic.keys():
        G.append([v[0], v[1], dic[v]])
        U[v[1]].append(v[0])
        V[v[0]].append(v[1])
    st1 = set()
    st1.add(n - 1)
    q = [n - 1]
    while len(q) > 0:
        t = q.pop(-1)
        for v in U[t]:
            if not v in st1:
                q.append(v)
                st1.add(v)
    st2 = set()
    st2.add(0)
    q = [0]
    while len(q) > 0:
        t = q.pop(-1)
        for v in V[t]:
            if not v in st2:
                q.append(v)
                st2.add(v)
    st = st1 & st2
    eg = []
    for v in G:
        if v[0] in st and v[1] in st:
            eg.append(v)
    ans = bellman_ford(0, n, eg)
    if ans is None:
        print(-1)
    else:
        print(max(0, -ans[n - 1]))


def __starting_point():
    main()


__starting_point()
