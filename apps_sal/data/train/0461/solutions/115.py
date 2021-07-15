class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = collections.defaultdict(list)
        for i,a in enumerate(manager):
            children[a].append(i)
        def dfs(i):
            if not children[i]:
                return 0
            else:
                return informTime[i]+max(dfs(j) for j in children[i])
        return dfs(children[-1][0])

