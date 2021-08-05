def main():
    # 行先、上限、逆辺
    def add_edge(From, to, cap):
        g[From][to] = cap
        g[to][-From - 1] = 0

    def max_flow(s, t):
        flow = 0
        while True:
            used = [False] * n
            used2 = [0] * n
            q = [(s, 10**6)]
            ans = [0]
            while q:
                v, f = q[-1]
                a = ans[0]
                if a == 0:
                    if v == t:
                        ans[0] = f
                        continue
                    gkv, gv = gkey[v], g[v]
                    l, used[v] = len(gkv), True
                    while True:
                        i = used2[v]
                        used2[v] += 1
                        if i < l:
                            to = gkv[i]
                            cap, to2 = gv[to], [to, -to - 1][to < 0]
                            if (not used[to2]) and cap:
                                q.append((to2, min(f, cap)))
                                break
                        else:
                            q.pop()
                            ans[0] = 0
                            break
                else:
                    q.pop()
                    if q:
                        v = q[-1][0]
                        i = used2[v] - 1
                        to = gkey[v][i]
                        g[v][to] -= a
                        g[[to, -to - 1][to < 0]][-v - 1] += a
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
