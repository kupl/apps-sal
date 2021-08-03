class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0

        buses_from_stops = defaultdict(set)
        for i, r in enumerate(routes):
            for v in r:
                buses_from_stops[v].add(i)

        memo = {}

        def check(bus, hist):
            if bus in memo:
                return memo[bus]

            if T in routes[bus]:
                return 1
            else:
                v = 1000000
                for stop in routes[bus]:
                    for bs in buses_from_stops[stop]:
                        if bs not in hist:
                            nh = set(hist)
                            nh.add(bs)
                            v = min(v, check(bs, nh))
                memo[bus] = v + 1
                return v + 1

        mn = 1000000
        for bs in buses_from_stops[S]:
            mn = min(mn, check(bs, set([bs])))
        return mn if mn < 1000000 else -1
