class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        stk = [(S, 0)]
        stop_dic = collections.defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_dic[stop].add(i)
                
        visited = set()
        while stk:
            stop, num_bus = stk.pop(0)
            if stop == T:
                return num_bus
            elif stop not in visited:
                visited.add(stop)
                buses = stop_dic[stop]
                for bus in buses:
                    for new_stop in routes[bus]:
                        if new_stop not in visited:
                            stk.append((new_stop, num_bus + 1))
                    routes[bus] = []
        return -1
