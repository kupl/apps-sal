class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(i, t):
            if i not in dic:
                self.ans = max(self.ans, t)
            for a, b in dic[i]:
                dfs(a, t + b)
        dic, self.ans = defaultdict(list), 0
        for i, m in enumerate(manager):
            dic[m].append((i, informTime[i]))
        dfs(dic[-1][0][0], dic[-1][0][1])
        return self.ans
