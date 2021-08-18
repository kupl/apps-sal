class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        graph = collections.defaultdict(list)
        for i, manager in enumerate(manager):
            graph[manager].append(i)

        def calculateTime(manager):

            if manager not in graph:
                return 0

            time = 0
            for emp in graph[manager]:
                time = max(calculateTime(emp), time)

            return time + informTime[manager]

        return calculateTime(headID)
