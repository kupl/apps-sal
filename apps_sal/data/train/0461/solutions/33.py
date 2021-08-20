class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        return self.DFS(n, headID, manager, informTime)

    def BFS(self, n: int, headID: int, manager: List[int], informTime: List[int]):
        graph = defaultdict(list)
        for i in range(n):
            graph[manager[i]].append((i, informTime[manager[i]]))
        q = deque([(headID, 0)])
        max_time = 0
        while q:
            (node, t) = q.popleft()
            max_time = max(max_time, t)
            for (sub_ord, inform_time) in graph[node]:
                q.append((sub_ord, inform_time + t))
        return max_time

    def DFS(self, n, headID, manager, informTime):
        graph = defaultdict(list)
        for i in range(n):
            graph[manager[i]].append((i, informTime[manager[i]]))

        def DFS_helper(node, graph, cur_time):
            nonlocal max_time
            max_time = max(max_time, cur_time)
            for (sub_ord, inform_time) in graph[node]:
                DFS_helper(sub_ord, graph, cur_time + inform_time)
        max_time = 0
        DFS_helper(headID, graph, 0)
        return max_time
