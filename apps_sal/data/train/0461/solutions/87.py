class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adjList = defaultdict(list)

        for i in range(n):
            # manager[i] = j so j -> i
            adjList[manager[i]].append(i)

        # starting at headID - BFS traversal
        queue = deque([(headID, 0)])

        # total time to inform
        maxTime = -1

        # manager[headID] subordinates to the CEO
        while queue:
            current, currentTime = queue.pop()
            # add all subordinates then add the time needed - repeat
            maxTime = max(maxTime, currentTime + informTime[current] )

            for employee in adjList[current]:
                queue.appendleft((employee, currentTime + informTime[current]))


        return maxTime
