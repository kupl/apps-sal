class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        bus_dic = defaultdict(set)
        for i, r in enumerate(routes):
            for s in r:
                bus_dic[s].add(i)

        seen = {S}
        av_bus = bus_dic[S]
        for bus in bus_dic[S]:
            if bus in bus_dic[T]:
                return 1
        cnt = 0
        while av_bus:
            tmp = set()
            cnt += 1
            for meh in range(len(av_bus)):
                bus = av_bus.pop()
                if bus in bus_dic[T]:
                    return cnt
                for s in routes[bus]:
                    if s not in seen:
                        seen.add(s)
                        for bus in bus_dic[s]:
                            if bus in bus_dic[T]:
                                return cnt + 1
                            tmp.add(bus)
            av_bus = tmp
        return -1
