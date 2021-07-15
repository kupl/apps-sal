class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        stops = collections.defaultdict(set)
        # stops = {1:[0], 2:[0], 7:[0,1], 3:[1], 6:[1]}
        # seen = 1, 2, 7
        # res = 
        # q = [2,7]
        # cur_st = 2
        for i in range(len(routes)):
            for st in routes[i]:
                stops[st].add(i)
        seen = {S}
        res = 0
        q = [S]
        while q:
            froniter = []
            while q:
                cur_st = q.pop()
                if cur_st == T:
                    return res
                for bus in stops[cur_st]:
                    for new_st in routes[bus]:
                        if new_st not in seen:
                            froniter.append(new_st)
                            seen.add(new_st)
            res += 1
            q = froniter
        
        return -1
