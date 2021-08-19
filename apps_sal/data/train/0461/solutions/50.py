class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        managerGraph = collections.defaultdict(list)
        for (i, v) in enumerate(manager):
            managerGraph[v].append(i)
        res = 0
        queue = collections.deque([(headID, 0)])
        while queue:
            (node, time) = queue.popleft()
            res = max(res, time)
            for nei in managerGraph[node]:
                queue.append((nei, time + informTime[node]))
        return res
