class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        from collections import defaultdict
        
        res = 0
        children = defaultdict(list)
        
        for i, e in enumerate(manager):
            children[e].append(i)
        queue = collections.deque([(headID, informTime[headID])])
        
        while queue:
            employeeID, time_needed = queue.popleft()
            res = max(res, time_needed)
            
            for child in children[employeeID]:
                queue.append((child, time_needed+informTime[child]))
        
        return res
