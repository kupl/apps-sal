from collections import defaultdict


class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        dist = {}
        depth = 0
        dist[S] = depth
        vis_bs = set()
        c_to_bs = defaultdict(list)
        for (pos_b, b) in enumerate(routes):
            for c in b:
                c_to_bs[c].append(pos_b)
        cur_cs = set([S])
        while len(cur_cs) > 0:
            depth += 1
            cur_bs = set()
            for c in cur_cs:
                for pos_b in c_to_bs[c]:
                    if pos_b not in vis_bs:
                        cur_bs.add(pos_b)
                vis_bs |= cur_bs
            cur_cs = set()
            for pos_b in cur_bs:
                for c in routes[pos_b]:
                    if c not in dist:
                        cur_cs.add(c)
                        dist[c] = depth
            if T in dist:
                return dist[T]
        return -1
