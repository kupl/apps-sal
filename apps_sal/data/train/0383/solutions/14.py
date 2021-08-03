class Solution:
    def dfs(self, i, visited, graph):
        if i in visited:
            return
        visited.add(i)
        for x, edge in enumerate(graph[i]):
            if edge:
                self.dfs(x, visited, graph)

    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        numInfected = float('inf')
        minVal = None
        initial.sort()
        for i in initial:
            visited = set([i])
            for j in initial:
                self.dfs(j, visited, graph)
            if len(visited) < numInfected:
                numInfected = len(visited)
                minVal = i

        return minVal
