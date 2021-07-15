class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(id: int) -> int:
            return max(informTime[id] + dfs(sub) for sub in subordinates[id]) if id in subordinates else 0
        
        subordinates = collections.defaultdict(list)
        for i, m in enumerate(manager):
            if i != headID:  #instead of m != -1
                subordinates.setdefault(m,[]).append(i)
        return dfs(headID)
