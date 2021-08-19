from queue import deque


class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        routes = list(map(set, routes))
        r_map = {}
        for (i, r1) in enumerate(routes):
            for j in range(i + 1, len(routes)):
                if len(r1 & routes[j]) > 0:
                    r_map.setdefault(i, []).append(j)
                    r_map.setdefault(j, []).append(i)
        (s_lst, t_lst) = ([], [])
        for (k, route) in enumerate(routes):
            if S in route:
                s_lst.append(k)
            if T in route:
                t_lst.append(k)
        if T in s_lst:
            return 1
        queue = deque([(idx, 1) for idx in s_lst])
        while len(queue) > 0:
            (curr_route, level) = queue.popleft()
            if curr_route in t_lst:
                return level
            if curr_route not in r_map:
                continue
            for dest in r_map[curr_route]:
                if dest not in s_lst:
                    s_lst.append(dest)
                    queue.append((dest, level + 1))
        return -1
