class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        employee_to_manager = collections.defaultdict(list)
        
        for i in range(len(manager)):
            employee_to_manager[manager[i]].append(i)
        queue = collections.deque()
        queue.append((headID, informTime[headID]))
        
        total_time = 0
        
        while queue:
            manager, t = queue.popleft()
            
            total_time = max(total_time, t)
            
            for employee in employee_to_manager[manager]:
                queue.append((employee, t +  informTime[employee]))
        return total_time
