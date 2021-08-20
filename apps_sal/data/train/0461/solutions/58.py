class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        m = collections.defaultdict(list)
        for (sub, mag) in enumerate(manager):
            m[mag].append(sub)

        def dfs(i):
            if not m[i]:
                return informTime[i]
            return max((dfs(j) for j in m[i])) + informTime[i]
        return dfs(headID)

        def dfs(i):
            if manager[i] != -1:
                informTime[i] += dfs(manager[i])
                manager[i] = -1
            return informTime[i]
        return max(list(map(dfs, list(range(len(manager))))))
