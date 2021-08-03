class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        from collections import defaultdict
        graph = defaultdict(list)
        for i, m in enumerate(manager):
            graph[m].append(i)

        to_inform = deque([(headID, informTime[headID])])
        max_t = 0
        while to_inform:
            m, t = to_inform.pop()
            max_t = max(max_t, t)
            for s in graph[m]:
                to_inform.append((s, t + informTime[s]))

        return max_t
