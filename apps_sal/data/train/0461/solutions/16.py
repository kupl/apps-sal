class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # create graph
        graph = collections.defaultdict(list)
        for idx, mgr in enumerate(manager):
            if idx == headID:
                continue 
                
            graph[mgr].append(idx)
        
        max_time = 0
        def dfs(start):
            nonlocal max_time
            if start is None:
                return 0
        
            curr_time = 0
            for child in graph[start]:
                curr_time = max(curr_time, dfs(child))
                
            max_time = max(max_time, curr_time + informTime[start])
            
            return curr_time + informTime[start]
        
        dfs(headID)
        
        return max_time
