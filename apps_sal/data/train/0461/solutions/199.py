class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n == 0:
            return 0
        if n == 1:
            return informTime[0]
        dic = collections.defaultdict(list)
        for i, x in enumerate(manager):
            if x != -1:
                dic[x].append(i)

        def dfs(node):
            time = 0
            if not dic[node]:
                return 0
            for sub in dic[node]:
                time = max(time, informTime[node] + dfs(sub))
            return time
        return dfs(headID)
