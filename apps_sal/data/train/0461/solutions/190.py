class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        

        reports = collections.defaultdict(set)
        
        for i, m in enumerate(manager):
            if m == -1:
                managerId = i
            else:
                reports[m].add(i)
            
        queue = collections.deque([(managerId, 0)])
        maxT = 0
        visited = set()
        while queue:
            person, time = queue.popleft()
            if person in visited:
                continue
                
            maxT = max(time, maxT)
            
            for r in reports[person]:
                queue.append((r, time + informTime[person]))
                
    
        return maxT
            

