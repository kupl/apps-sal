
class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        numNodes = len(graph)
        minSpread = float('inf')
        minNode = None
        initial.sort()
        
        def helper(curr, visited):

            if curr in visited:
                return

            edges = graph[curr]
            visited.add(curr)

            for i in range(len(edges)):
                if graph[curr][i] == 1:
                    helper(i, visited)     
        
        for i in initial:
            visited = set([i])
            for j in initial:
                if i!= j:
                    helper(j, visited)
          
            if len(visited) < minSpread:
                minSpread = len(visited)
                minNode = i
        
        return minNode
        
    

