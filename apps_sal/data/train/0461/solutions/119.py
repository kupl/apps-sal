class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = [[] for i in range(n)]
        for (person, manag) in enumerate(manager):
            if manag != -1:
                children[manag].append(person)

        def dfs(node):
            return max((dfs(child) for child in children[node]), default=0) + informTime[node]
        return dfs(headID)
