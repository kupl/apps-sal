class Solution:

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        memo = [float('-inf')] * (n + 1)
        score = 0

        @lru_cache
        def dfs(start, score=0):
            for i in range(start, min(n, start + 3)):
                score += stoneValue[i]
                memo[start] = max(memo[start], score - dfs(i + 1))
            return memo[start] if memo[start] != float('-inf') else 0
        return 'Tie' if dfs(0) == 0 else 'Alice' if dfs(0) > 0 else 'Bob'
