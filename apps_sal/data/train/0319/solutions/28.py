class Solution:

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        prefix = [0] * (len(stoneValue) + 1)
        for i in range(len(stoneValue)):
            prefix[i + 1] = prefix[i] + stoneValue[i]
        memo = {}
        aliceScore = self.dfs(stoneValue, 0, memo, prefix)
        total = sum(stoneValue)
        if total - aliceScore > aliceScore:
            return 'Bob'
        elif total - aliceScore < aliceScore:
            return 'Alice'
        return 'Tie'

    def dfs(self, stoneValue, i, memo, prefix):
        if i == len(stoneValue):
            return 0
        if i in memo:
            return memo[i]
        ans = stoneValue[i] + prefix[-1] - prefix[i + 1] - self.dfs(stoneValue, i + 1, memo, prefix)
        if i + 1 < len(stoneValue):
            ans = max(ans, stoneValue[i] + stoneValue[i + 1] + prefix[-1] - prefix[i + 2] - self.dfs(stoneValue, i + 2, memo, prefix))
        if i + 2 < len(stoneValue):
            ans = max(ans, stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] + prefix[-1] - prefix[i + 3] - self.dfs(stoneValue, i + 3, memo, prefix))
        memo[i] = ans
        return memo[i]
