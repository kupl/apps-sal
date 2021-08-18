class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        memo = {}

        def dfs(stoneValue, i, memo):
            if i in memo:
                return memo[i]
            if i >= len(stoneValue):
                return 0
            if i == len(stoneValue) - 1:
                return stoneValue[i]

            maxi = stoneValue[i] + min(dfs(stoneValue, i + 2, memo), dfs(stoneValue, i + 3, memo), dfs(stoneValue, i + 4, memo))
            if i + 1 < len(stoneValue):
                maxi = max(maxi, stoneValue[i] + stoneValue[i + 1] + min(dfs(stoneValue, i + 3, memo), dfs(stoneValue, i + 4, memo), dfs(stoneValue, i + 5, memo)))
            if i + 2 < len(stoneValue):
                maxi = max(maxi, sum(stoneValue[i:i + 3]) + min(dfs(stoneValue, i + 4, memo), dfs(stoneValue, i + 5, memo), dfs(stoneValue, i + 6, memo)))
            memo[i] = maxi
            return maxi

        aliceScore = dfs(stoneValue, 0, memo)
        bobScore = sum(stoneValue) - aliceScore

        if aliceScore > bobScore:
            return 'Alice'

        elif aliceScore < bobScore:
            return 'Bob'

        return 'Tie'
