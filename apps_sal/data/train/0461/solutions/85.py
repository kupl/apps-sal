class Solution:
    class AdjList:
        def __init__(self, edges, h):
            self.manager = edges
            self.mlist = {}
            for u, v in enumerate(edges):

                if v == -1:
                    continue
                if u not in self.mlist:
                    self.mlist[u] = [v]
                else:
                    self.mlist[u].append(v)

                if v not in self.mlist:
                    self.mlist[v] = [u]
                else:
                    self.mlist[v].append(u)

        def adjacent(self, node):

            if node not in self.mlist:
                return []

            return self.mlist[node]

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        adj = Solution.AdjList(manager, headID)

        visited = [0] * n

        def dfs(node):

            visited[node] = 1

            t = 0
            for neig in adj.adjacent(node):

                if visited[neig] == 0:
                    temp = dfs(neig)
                    t = max(t, temp)

            return informTime[node] + t

        return dfs(headID)
