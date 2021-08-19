from collections import defaultdict, deque


class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T or not routes:
            return 0
        mapping = defaultdict(list)
        for (i, route) in enumerate(routes):
            for start in route:
                mapping[start].append(i)
        q = deque([[S, 0]])
        while q:
            (prev_stop, dist) = q.popleft()
            if prev_stop not in mapping:
                continue
            bus_num_li = mapping[prev_stop]
            mapping[prev_stop] = []
            for cur_bus_num in bus_num_li:
                new_dist = dist + 1
                for cur_stop in routes[cur_bus_num]:
                    if cur_stop == T:
                        return new_dist
                    q.append([cur_stop, new_dist])
                routes[cur_bus_num] = []
        return -1
