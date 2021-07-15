class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        res = [[0 for _ in range(target + 1)] for _ in range(d + 1)]
        modula = (10**9)+7
        res[0][0] = 1
        for dice in range(1, d + 1):
            for i in range(dice, target + 1):
                interestMinRange = max(0, i - f)
                res[dice][i] = sum(res[dice - 1][interestMinRange:i]) % modula
        return res[-1][-1]
                

