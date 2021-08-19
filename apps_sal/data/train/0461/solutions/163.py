from collections import defaultdict


class Solution:
    # time for a manager = time[employee] + time[manager]
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # [manager1, manager2...]
        # 0th employee, 1st employee
        mp = defaultdict(list)  # {manager: [employee id]}
        for i in range(n):
            if manager[i] != -1:
                mp[manager[i]].append(i)

        def find_time(manager):
            employees = mp[manager]
            maxval = 0
            for employee in employees:
                maxval = max(maxval, find_time(employee))
            return maxval + informTime[manager]

        return find_time(headID)
