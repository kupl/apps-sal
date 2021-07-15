class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        s2b = defaultdict(set)
        for b in range(len(routes)):
            routes[b] = set(routes[b])
            for s in routes[b]:
                s2b[s].add(b)
        
        visited = set()
        q = [(1, b) for b in s2b[S]]
        while q:
            n, b = q.pop(0)
            if b in visited:
                continue
            visited.add(b)
            bs = set()
            for s in routes[b]:
                if s == T:
                    return n
                bs |= s2b[s]
            for bn in bs:
                q.append((n + 1, bn))
            
        return -1
