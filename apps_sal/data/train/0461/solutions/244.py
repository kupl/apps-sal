class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordination = collections.defaultdict(list)
        for i, mID in enumerate(manager):
            if mID != -1:
                subordination[mID].append(i)

        def dfs(mID: int) -> int:
            maxTime = 0
            for sub in subordination[mID]:
                maxTime = max(maxTime, informTime[mID] + dfs(sub))
            return maxTime

        return dfs(headID)
