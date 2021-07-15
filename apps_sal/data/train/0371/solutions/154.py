class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        hmap = collections.defaultdict(set)
        
        for i in range(len(routes)):
            for j in routes[i]:
                hmap[j].add(i) # adjacency list for route to bus... i.e. tracking the stop on each route.
        # print(hmap)
        q = [(S, 0)]
        visited = set()
        visited.add(S)
        
        while q:
            stop, buses = q.pop(0)
            
            if stop == T:
                return buses
            
            for i in hmap[stop]: # go to the ith bus route
                # print(i)
                for j in routes[i]: # traverse the ith bus route
                    if j not in visited:
                        visited.add(j)
                        q.append((j, buses + 1))
        
        return -1
