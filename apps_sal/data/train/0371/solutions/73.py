from collections import defaultdict, deque


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if(S == T):
            return 0
        circuits = defaultdict(list)
        rel = {}
        for i in range(len(routes)):
            for stand in routes[i]:
                circuits[stand].append(i)
                rel[(i, stand)] = 1
        vis = {i: 1 for i in circuits[S]}
        vis_bus = {S: 1}
        q = deque([i for i in circuits[S]])
        level = 1
        while q:
            l = len(q)
            for i in range(l):
                curr_cir = q.popleft()
                if((curr_cir, T) in rel):
                    return level
                for bus in routes[curr_cir]:
                    if bus not in vis_bus:
                        vis_bus[bus] = 1
                        for cir in circuits[bus]:
                            if cir not in vis:
                                q.append(cir)
                                vis[cir] = 1
            level += 1
        return -1
