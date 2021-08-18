class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        res = 0
        graph = defaultdict(list)
        for index, parent in enumerate(manager):
            graph[parent].append(index)

        queue = deque([(headID, informTime[headID])])
        while queue:
            curId, curTime = queue.popleft()
            res = max(res, curTime)
            for child in graph[curId]:
                queue.append((child, curTime + informTime[child]))
        return res
