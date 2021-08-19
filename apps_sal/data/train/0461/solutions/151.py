class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinates = collections.defaultdict(list)
        for i in range(n):
            subordinates[manager[i]].append(i)
        queue = collections.deque([(headID, 0)])
        max_time = 0
        while queue:
            (employee_mgr, time) = queue.popleft()
            max_time = max(max_time, time)
            queue.extend(((employee, time + informTime[employee_mgr]) for employee in subordinates[employee_mgr]))
        return max_time
