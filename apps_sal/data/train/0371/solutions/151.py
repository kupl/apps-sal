class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        bus_stop_dict = collections.defaultdict(set)
        for i in range(len(routes)):
            for stop in routes[i]:
                bus_stop_dict[stop].add(i)
        seen_bus = set()
        seen_stop = set()
        stop_list = []
        for bus in bus_stop_dict[S]:
            seen_bus.add(bus)
            for stop in routes[bus]:
                if stop not in seen_stop:
                    seen_stop.add(stop)
                    stop_list.append(stop)
        ans = 1
        while stop_list:
            new_list = []
            for stop in stop_list:
                seen_stop.add(stop)
                if stop == T:
                    return ans
                for bus in bus_stop_dict[stop]:
                    if bus not in seen_bus:
                        seen_bus.add(bus)
                    for s in routes[bus]:
                        if s not in seen_stop:
                            seen_stop.add(s)
                            new_list.append(s)
            stop_list = new_list
            ans += 1
        return -1
