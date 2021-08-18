class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        memo = {}

        def dfs(start):
            if start >= len(stoneValue):
                return 0
            if start in memo:
                return memo[start]
            memo[start] = -math.inf
            score = 0
            for i in range(start, min(len(stoneValue), start + 3)):
                score += stoneValue[i]
                memo[start] = max(memo[start], score - dfs(i + 1))

            return memo[start]
        score = dfs(0)

        if score > 0:
            return 'Alice'
        elif score == 0:
            return 'Tie'
        else:
            return 'Bob'
