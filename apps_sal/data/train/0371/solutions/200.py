from queue import deque


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        # 1. create map of route_idx to List[route_idx]
        # if two routes have same bus stops, attach edge to map.
        # 2. go through routes, if any route has S,
        # store idx of this route in s_lst;
        # if any route has T, store idx this route in t_lst.
        # 3. BFS queue of (route_idx, depth)

        # base cases
        if S == T:
            return 0
        # 1
        routes = list(map(set, routes))
        r_map = {}  # route_idx to List[route_idx]
        for i, r1 in enumerate(routes):
            for j in range(i + 1, len(routes)):
                if len(r1 & routes[j]) > 0:
                    r_map.setdefault(i, []).append(j)
                    r_map.setdefault(j, []).append(i)
        # 2.
        # NOTE: s_lst also functions as visitied lst.
        s_lst, t_lst = [], []
        for k, route in enumerate(routes):
            if S in route:
                s_lst.append(k)
            if T in route:
                t_lst.append(k)

        # base case
        if T in s_lst:
            return 1
        # 3.
        queue = deque([(idx, 1) for idx in s_lst])
        while len(queue) > 0:
            curr_route, level = queue.popleft()
            if curr_route in t_lst:
                return level
            if curr_route not in r_map:
                # dead end, no other routes overlap with curr
                continue
            for dest in r_map[curr_route]:
                if dest not in s_lst:
                    s_lst.append(dest)
                    queue.append((dest, level + 1))
        return -1
