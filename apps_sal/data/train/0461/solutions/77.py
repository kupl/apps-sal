class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        if n == 1:
            return 0

        time = collections.defaultdict(int)

        worksUnder = collections.defaultdict(set)

        for i in range(n):
            worksUnder[manager[i]].add(i)

        stack = [headID]
        while stack:
            managerID = stack.pop()
            for i in worksUnder[managerID]:
                time[i] = informTime[managerID] + time[managerID]
                stack.append(i)

        return max(time.values())
