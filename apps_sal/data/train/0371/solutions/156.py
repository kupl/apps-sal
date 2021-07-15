class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        if S == T: 
            return 0
        
        
        # routes = map(set, routesList)
        for i, route in enumerate(routes):
            routes[i] = set(route)
        print(routes)
        
        graph = collections.defaultdict(set)
        for i, r1 in enumerate(routes):
            for j in range(i+1, len(routes)):
                r2 = routes[j]
                if any(r in r2 for r in r1):
                    graph[i].add(j)
                    graph[j].add(i)
                    
        print(graph)

        seen, targets = set(), set()
        for node, route in enumerate(routes):
            if S in route: 
                seen.add(node)
            if T in route: 
                targets.add(node)

        queue = [(node, 1) for node in seen]
        for node, depth in queue:
            if node in targets: 
                return depth
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth+1))
        return -1
