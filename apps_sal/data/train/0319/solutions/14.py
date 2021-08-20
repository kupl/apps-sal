class Solution:

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        mem = {}

        def helper(stoneValues, index):
            if index in mem:
                return mem[index]
            if index >= len(stoneValues):
                return 0
            ans = stoneValues[index] - helper(stoneValues, index + 1)
            if index + 1 < len(stoneValues):
                temp = stoneValues[index] + stoneValues[index + 1] - helper(stoneValues, index + 2)
                ans = max(ans, temp)
            if index + 2 < len(stoneValues):
                temp = stoneValues[index] + stoneValues[index + 1] + stoneValues[index + 2] - helper(stoneValues, index + 3)
                ans = max(ans, temp)
            mem[index] = ans
            return ans
        ans = helper(stoneValue, 0)
        if ans > 0:
            return 'Alice'
        elif ans < 0:
            return 'Bob'
        return 'Tie'
