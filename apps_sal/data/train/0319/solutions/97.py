class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        mem = {i: 0 for i in range(len(stoneValue) + 1)}
        mem1, mem2, mem3 = 0, 0, 0
        i = len(stoneValue) - 1
        while i >= 0:
            ans = stoneValue[i] - mem1
            if i + 1 < len(stoneValue):
                ans = max(ans, stoneValue[i] + stoneValue[i + 1] - mem2)
            if i + 2 < len(stoneValue):
                ans = max(ans, stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - mem3)
            mem3 = mem2
            mem2 = mem1
            mem1 = ans
            i -= 1
        if ans > 0:
            return 'Alice'
        elif ans < 0:
            return 'Bob'
        return 'Tie'
