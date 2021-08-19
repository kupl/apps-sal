class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adjList = defaultdict(list)
        for i in range(n):
            adjList[manager[i]].append(i)
        queue = deque([(headID, 0)])
        maxTime = -1
        while queue:
            (current, currentTime) = queue.pop()
            maxTime = max(maxTime, currentTime + informTime[current])
            for employee in adjList[current]:
                queue.appendleft((employee, currentTime + informTime[current]))
        return maxTime
