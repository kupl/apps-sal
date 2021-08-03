class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(node, cur_time):
            nonlocal total_time
            visited.add(node)
            total_time = max(total_time, cur_time)
            for next_node in graph[node]:
                if next_node not in visited:
                    dfs(next_node, cur_time + informTime[node])

        total_time = 0
        graph = defaultdict(set)
        for u, v in enumerate(manager):
            graph[u].add(v)
            graph[v].add(u)
        visited = set()
        visited.add(-1)

        dfs(headID, 0)
        return total_time
