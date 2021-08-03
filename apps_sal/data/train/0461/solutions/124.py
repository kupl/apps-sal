class Solution:
    def dfsFromId(self, g, visited, informTime, vertex, times, currTime):
        visited[vertex] = True
        times[0] = max(times[0], currTime)
        for to in g[vertex]:
            if not visited[to]:
                self.dfsFromId(g, visited, informTime, to, times, currTime + informTime[vertex])

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        g = [set() for i in range(n)]
        visited = [False] * n
        maxMinutes = [0]

        for i, v in enumerate(manager):
            g[v].add(i)

        self.dfsFromId(g, visited, informTime, headID, maxMinutes, 0)

        return maxMinutes[0]
