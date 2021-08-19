class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = {i: [] for i in range(n)}
        for i in range(n):
            if manager[i] >= 0:
                graph[manager[i]].append(i)
        to_inform = deque([(headID, 0)])
        max_t = 0
        while to_inform:
            (mid, t) = to_inform.pop()
            new_t = t + informTime[mid]
            max_t = max(max_t, new_t)
            for s in graph[mid]:
                to_inform.append((s, new_t))
        return max_t
