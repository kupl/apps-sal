class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = collections.defaultdict(list)
        for i in range(n):
            graph[manager[i]].append(i)

        queue = collections.deque([(headID, 0)])
        result = 0
        while queue:
            i, time = queue.pop()
            result = max(result, time)
            for j in graph[i]:
                queue.append((j, time + informTime[i]))
        return result
