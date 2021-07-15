class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if T == S:
            return 0
        possibleStarts = []
        possibleEnd = []
        stopGraph = {}
        for i, route in enumerate(routes):
            for stop in route:
                if stop == S:
                    possibleStarts.append(i)
                elif stop == T:
                    possibleEnd.append(i)
                
                if stop in stopGraph:
                    stopGraph[stop].append(i)
                else:
                    stopGraph[stop] = [i]
        
#         {7: [1, 0, 2],
#         8: [2, 0, 4]}
        
#         { 1:[0, 2],0:[1, 2], 2:[0, 1, 3, 4], 3:[2, 4], 4:[2, 3]}
        
        graph = {}
        for stop in list(stopGraph.keys()):
            validRoutes = stopGraph[stop]
            if len(stopGraph[stop]) <= 1:
                continue
            for route in validRoutes:
                if route not in graph:
                    graph[route] = set()
                for x in validRoutes:
                    if x != route:
                        graph[route].add(x)                  
        # print(graph)
        # print(stopGraph)
        # print(possibleStarts)
        # print(possibleEnd)
        queue = [(x, 1) for x in possibleStarts]
        seen = set()
        while queue:
            node = queue.pop(0)
            seen.add(node[0])
            if node[0] in possibleEnd:
                return node[1]
            if node[0] in graph:
                children = graph[node[0]]
            
                for child in children:
                    if child not in seen:
                        queue.append((child, node[1] + 1))
                        seen.add(child)

            
                
        return -1
        
                    
        

