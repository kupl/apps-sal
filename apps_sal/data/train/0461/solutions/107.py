from collections import defaultdict as dd

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        m_to_s = dd(set)
        for i in range(len(manager)):
            m_to_s[manager[i]].add(i)
        stack = [(headID, 0)]
        max_time = 0
        while stack:
            employee, time = stack.pop()
            max_time = max(time, max_time)
            for subordinate in m_to_s[employee]:
                stack.append((subordinate, time + informTime[employee]))
        return max_time
