from collections import defaultdict


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if len(manager) <= 1:
            return informTime[headID]

        graph = defaultdict(list)

        q = deque()

        def bfs(graph):
            time_so_far = 0
            while q:
                node, time_taken = q.popleft()
                time_so_far = max(time_so_far, time_taken)
                for next_node in graph[node]:
                    q.append([next_node, time_taken + informTime[next_node]])
            return time_so_far

        for m in range(len(manager)):
            if manager[m] != -1:
                graph[manager[m]].append(m)

        q.append([headID, informTime[headID]])

        return bfs(graph)
