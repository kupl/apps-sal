class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = [-float('inf')] * (len(stoneValue) + 5)
        dp[len(stoneValue):len(stoneValue) + 5] = [0] * 5
        postfix = [0] * (len(stoneValue) + 1)
        for i in range(len(stoneValue) - 1, -1, -1):
            postfix[i] = postfix[i + 1] + stoneValue[i]
        s = stoneValue

        dp = dict()

        def search(i):
            if i >= len(stoneValue):
                return 0
            res = -float('inf')
            score = 0
            if i in dp:
                return dp[i]
            for j in range(3):
                if i + j < len(stoneValue):
                    score += stoneValue[i + j]
                    res = max(score - search(i + j + 1), res)
            dp[i] = res
            return dp[i]

        ans = search(0)
        if dp[0] == 0:
            return 'Tie'
        return 'Alice' if dp[0] > 0 else 'Bob'
