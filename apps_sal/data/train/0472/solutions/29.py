class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        graph = [set() for _ in range(n)]
        for i, j in enumerate(arr):
            if i+j < n:
                graph[i].add(i+j)
            if i-j >= 0:
                graph[i].add(i-j)
                
        self.graph = graph        
        self.visited = set()
        return self.dfs(start)
        
    def dfs(self, i):
        if i in self.visited:
            return False
        self.visited.add(i)
        if i in self.graph[i]:
            return True
        else:
            for j in self.graph[i]:
                if self.dfs(j):
                    return True
