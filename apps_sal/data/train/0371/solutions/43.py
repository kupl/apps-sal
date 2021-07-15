class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        
#         if S==T:
#             return 0
#         graph=collections.defaultdict(list)
#         for i,stops in enumerate(routes):
#             for s in stops:
#                 graph[s].append(i)
#         que=graph[S]
#         visited=set()
#         steps=0
#         while que:
#             tmp=[]
#             for bus in que:
#                 if bus in visited:
#                     continue
#                 visited.add(bus)
#                 for stop in routes[bus]:
#                     if stop==T:
#                         return steps+1
#                     for bus2 in graph[stop]:
#                         if bus2 not in visited:
#                             tmp.append(bus2)
#             que=tmp
#             steps+=1
#         return -1
        if S == T: return 0
        routes = list(map(set, routes))
        graph = collections.defaultdict(set)
        for i, r1 in enumerate(routes):
            for j in range(i+1, len(routes)):
                r2 = routes[j]
                if any(r in r2 for r in r1):
                    graph[i].add(j)
                    graph[j].add(i)

        seen, targets = set(), set()
        for node, route in enumerate(routes):
            if S in route: seen.add(node)
            if T in route: targets.add(node)

        queue = [(node, 1) for node in seen]
        for node, depth in queue:
            if node in targets: return depth
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth+1))
        return -1

