class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = [[] for i in range(n)]
        # construct the tree
        # children[m] is the list of direct subordinates
        # of m
        for i, m in enumerate(manager):
            if m >= 0:
                children[m].append(i)
        
        # the time for a maganer = max(his employee's time)
        # + inforTime[manager]
        def dfs(i):
            return max([dfs(j) for j in children[i]] or [0]) + informTime[i]
        
        return dfs(headID)
