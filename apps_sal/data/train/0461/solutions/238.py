class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # Convert to a tree structure
        
        graph = collections.defaultdict(list)
        for person, boss in enumerate(manager):
            if boss != -1:
                graph[boss].append(person)
            
        # Then do a bfs
        # Person with max_time is the answer
        # Guaranteed to be a tree, no need for seen
        queue = [(headID, 0)]
        max_time = - float('inf')
        
        while queue:
            nq = []
            
            for boss, time in queue:
                max_time = max(max_time, time)
                
                for employee in graph[boss]:
                    nq.append((employee, time + informTime[boss]))
            queue = nq
            
        return max_time
