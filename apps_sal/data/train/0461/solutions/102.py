class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = defaultdict(list)
        for i, j in enumerate(manager):
            children[j].append(i)
        
        def dfs(node):
            return informTime[node] + max([dfs(child) for child in children[node]] or [0])
        
        return dfs(headID)
