class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        from collections import defaultdict

        res = 0

        children = defaultdict(list)

        for i, e in enumerate(manager):
            children[e].append(i)

        stack = [(headID, informTime[headID])]

        while stack:
            employeeID, time_needed = stack.pop()
            res = max(res, time_needed)

            for child in children[employeeID]:
                stack.append((child, time_needed + informTime[child]))

        return res
