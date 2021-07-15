def main():
    import dataclasses
    from heapq import heappush, heappop

    @dataclasses.dataclass(frozen=True)
    class Path:
        to: int
        fare: int
        travel_time: int

    @dataclasses.dataclass(frozen=True)
    class ExchangeRate:
        Ag: int
        exchange_time: int

    @dataclasses.dataclass(frozen=True)
    class Traveler:
        consumption_time: int
        remaining_Ag: int
        location: int

        def __gt__(self, other):
            return self.consumption_time > other.consumption_time

        def __eq__(self, other):
            return self.consumption_time == other.consumption_time

    INF = 1 << 60
    MX_AG = 2500

    N, M, S = list(map(int, input().split()))
    S = min(S, MX_AG)  # それ以上のAgは不要

    g = tuple(set() for _ in range(N))
    for _ in range(M):
        u, v, a, b = list(map(int, input().split()))
        u -= 1
        v -= 1
        g[u].add(Path(v, a, b))
        g[v].add(Path(u, a, b))

    exchange = []
    for _ in range(N):
        c, d = list(map(int, input().split()))
        exchange.append(ExchangeRate(c, d))

    h = [Traveler(0, S, 0)]

    time = [[INF] * (MX_AG + 1) for _ in range(N)]
    time[0][S] = 0
    # time[location][r_Ag]:=minimum_time_to_reach

    while h:
        t = heappop(h)
        for p in g[t.location]:
            n_Ag = t.remaining_Ag - p.fare
            if n_Ag < 0: continue
            cf = time[p.to][n_Ag]
            n_time = t.consumption_time + p.travel_time
            if cf <= n_time: continue
            time[p.to][n_Ag] = n_time
            heappush(h, Traveler(consumption_time=n_time, remaining_Ag=n_Ag, location=p.to))

        e_time = t.consumption_time + exchange[t.location].exchange_time
        e_Ag = t.remaining_Ag + exchange[t.location].Ag
        if e_Ag > MX_AG: continue
        cf = time[t.location][e_Ag]
        if cf <= e_time: continue
        time[t.location][e_Ag] = e_time
        heappush(h, Traveler(consumption_time=e_time, remaining_Ag=e_Ag, location=t.location))

    for to in range(1, N):
        print((min(time[to])))


def __starting_point():
    main()

__starting_point()
