def main():
    from heapq import heappush, heappop
    INF = 1 << 60
    MX_AG = 2500
    (N, M, S) = map(int, input().split())
    S = min(S, MX_AG)
    g = tuple((set() for _ in range(N)))
    for _ in range(M):
        (u, v, a, b) = map(int, input().split())
        u -= 1
        v -= 1
        g[u].add((v, a, b))
        g[v].add((u, a, b))
    exchange = []
    for _ in range(N):
        (c, d) = map(int, input().split())
        exchange.append((c, d))
    h = [(0, S, 0)]
    time = [[INF] * (MX_AG + 1) for _ in range(N)]
    time[0][S] = 0
    while h:
        (t, ag, loc) = heappop(h)
        for (to, fare, dt) in g[loc]:
            n_Ag = ag - fare
            if n_Ag < 0:
                continue
            cf = time[to][n_Ag]
            n_time = t + dt
            if cf <= n_time:
                continue
            time[to][n_Ag] = n_time
            heappush(h, (n_time, n_Ag, to))
        e_time = t + exchange[loc][1]
        e_Ag = ag + exchange[loc][0]
        if e_Ag > MX_AG:
            continue
        cf = time[loc][e_Ag]
        if cf <= e_time:
            continue
        time[loc][e_Ag] = e_time
        heappush(h, (e_time, e_Ag, loc))
    ans = (min(time[to]) for to in range(1, N))
    print(*ans, sep='\n')


def __starting_point():
    main()


__starting_point()
