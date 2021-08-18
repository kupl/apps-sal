def main():
    def add_edge(From, to, cap):
        g[From][to] = cap
        g[to][-From - 1] = 0

    def max_flow(s, t):
        def dfs():
            while q:
                v, t, f = q[-1]
                if ans[0] == 0:
                    if v == t:
                        ans[0] = f
                        continue
                    used[v] += 1
                    while True:
                        i = used2[v]
                        used2[v] += 1
                        if i < len(gkey[v]):
                            to = gkey[v][i]
                            cap = g[v][to]
                            if to < 0:
                                to2 = -to - 1
                            else:
                                to2 = to
                            if used[to2] or cap == 0:
                                continue
                            q.append((to2, t, min(f, cap)))
                            break
                        else:
                            q.pop()
                            ans[0] = 0
                            break
                else:
                    q.pop()
                    if q:
                        v, t, f = q[-1]
                        i = used2[v] - 1
                        to = gkey[v][i]
                        if to < 0:
                            to2 = -to - 1
                        else:
                            to2 = to
                        g[v][to] -= ans[0]
                        g[to2][-v - 1] += ans[0]

        flow = 0
        while True:
            used = [0] * n
            used2 = [0] * n
            q = [(s, t, 10**6)]
            ans = [0]
            dfs()
            if not ans[0]:
                return flow
            flow += ans[0]

    h, w = list(map(int, input().split()))
    n = h + w + 2
    g = [dict() for _ in range(n)]
    for i in range(h):
        A = input()
        for j in range(w):
            if A[j] == "o":
                add_edge(i, j + h, 1)
                add_edge(j + h, i, 1)
            elif A[j] == "S":
                add_edge(h + w, i, 10**6)
                add_edge(h + w, j + h, 10**6)
            elif A[j] == "T":
                add_edge(i, h + w + 1, 10**6)
                add_edge(j + h, h + w + 1, 10**6)
    gkey = [list(i.keys()) for i in g]

    ans = max_flow(h + w, h + w + 1)
    if ans >= 10**6:
        print((-1))
    else:
        print(ans)


main()
