def main():
    import sys
    sys.setrecursionlimit(1000000)

    def add_edge(From, to, cap):
        g[From][to] = cap
        g[to][-From - 1] = 0

    def max_flow(s, t):

        def dfs(v, t, f):
            q.append(v)
            if v == t:
                return f
            used[v] += 1
            for i in range(len(gkey[v])):
                to = gkey[v][i]
                cap = g[v][to]
                if to < 0:
                    to2 = -to - 1
                else:
                    to2 = to
                if used[to2] or cap == 0:
                    continue
                d = dfs(to2, t, min(f, cap))
                if d > 0:
                    g[v][to] -= d
                    g[to2][-v - 1] += d
                    return d
            q.pop()
            return 0
        flow = 0
        while True:
            used = [0] * n
            q = []
            f = dfs(s, t, 10 ** 100)
            if not q:
                return flow
            flow += f
    (h, w) = list(map(int, input().split()))
    n = h + w + 2
    g = [dict() for _ in range(n)]
    for i in range(h):
        A = input()
        for j in range(w):
            if A[j] == 'o':
                add_edge(i, j + h, 1)
                add_edge(j + h, i, 1)
            elif A[j] == 'S':
                add_edge(h + w, i, 10 ** 6)
                add_edge(h + w, j + h, 10 ** 6)
            elif A[j] == 'T':
                add_edge(i, h + w + 1, 10 ** 6)
                add_edge(j + h, h + w + 1, 10 ** 6)
    gkey = [list(i.keys()) for i in g]
    ans = max_flow(h + w, h + w + 1)
    if ans >= 10 ** 6:
        print(-1)
    else:
        print(ans)


main()
