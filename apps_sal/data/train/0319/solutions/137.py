class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # --- corner case
        if not stoneValue:
            return 'Tie'

        #--- setup
        n = len(stoneValue)
        dp = [0 for _ in range(n + 3)]
        stoneValue = stoneValue + [0, 0, 0]
        #--- main
        for i in range(n - 1, -1, -1):
            max_v = float('-inf')
            curr = stoneValue[i]
            for j in range(i + 1, i + 4):
                max_v = max(max_v, curr - dp[j])
                curr += stoneValue[j]
            dp[i] = max_v
        # print(dp)
        if dp[0] > 0:
            return 'Alice'
        if dp[0] < 0:
            return 'Bob'
        return 'Tie'
