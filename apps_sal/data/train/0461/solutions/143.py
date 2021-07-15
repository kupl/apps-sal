class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        reports = collections.defaultdict(list)
        for i, m in enumerate(manager):
            reports[m].append(i)
        
        def dfs(i):
            return informTime[i] + max([dfs(r) for r in reports[i]], default=0) 
        
        return dfs(headID)
