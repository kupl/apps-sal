class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        n = len(routes)
        graph = defaultdict(set)
        
        for i, r in enumerate(routes):
            for s in r:
                graph[s].add(i)
        
        q = [(S, 0)]
        visit = set()
        visit.add(S)

        while q:
            cur, dis = q.pop(0)
            
            if cur == T:
                return dis
            
            for r in graph[cur]:
                for j in routes[r]:
                    if j not in visit:
                        q.append((j, dis+1))
                        visit.add(j)
 
        return -1
