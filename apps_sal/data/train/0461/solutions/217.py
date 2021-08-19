from typing import List
from collections import defaultdict


class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        def build_graph():
            g = defaultdict(list)
            for employee_id in range(n):
                manager_id = manager[employee_id]
                if manager_id == -1:
                    continue
                g[manager_id].append(employee_id)
            return g
        g = build_graph()
        max_time = [0]

        def dfs(total_time, employee_id):
            if employee_id not in g:
                max_time[0] = max(total_time, max_time[0])
                return
            subordinates = g[employee_id]
            for subordinate in subordinates:
                dfs(total_time + informTime[employee_id], subordinate)
        dfs(0, headID)
        return max_time[0]
