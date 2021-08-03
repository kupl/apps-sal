class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = collections.defaultdict(list)
        for idx in range(n):
            graph[manager[idx]].append(idx)

        max_time = 0
        queue = collections.deque([(headID, 0)])
        while queue:
            node, time = queue.popleft()
            max_time = max(max_time, time)
            for sub in graph[node]:
                queue.append((sub, time + informTime[node]))
        return max_time
