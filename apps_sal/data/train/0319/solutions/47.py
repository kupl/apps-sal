class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        cursum = 0
        dp1 = [float('-inf')] * (n + 1)
        dp1[-1] = 0
        for i in range(n - 1, -1, -1):
            cursum += stoneValue[i]
            for k in range(3):
                if i + k >= n:
                    break
                dp1[i] = max(dp1[i], cursum - dp1[i + k + 1])
        if dp1[0] > cursum - dp1[0]:
            return 'Alice'
        if dp1[0] < cursum - dp1[0]:
            return 'Bob'
        return 'Tie'
