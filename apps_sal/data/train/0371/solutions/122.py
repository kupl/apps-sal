class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        stop_bus = collections.defaultdict(set)
        for i in range(len(routes)):
            for stop in routes[i]:
                stop_bus[stop].add(i)
        if S not in list(stop_bus.keys()) or T not in list(stop_bus.keys()):
            return -1
        if S == T:
            return 0
        q = [x for x in stop_bus[S]]
        seen = set([x for x in stop_bus[S]])
        cnt = 0
        while q:
            cnt += 1
            for _ in range(len(q)):
                cur_bus = q.pop(0)
                if T in routes[cur_bus]:
                    return cnt
                else:
                    for stop in routes[cur_bus]:
                        for bus in stop_bus[stop]:
                            if bus not in seen:
                                seen.add(cur_bus)
                                q.append(bus)
        return -1
