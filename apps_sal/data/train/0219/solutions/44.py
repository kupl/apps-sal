class Solution:

    def longestWPI(self, hours: List[int]) -> int:
        presum = 0
        res = 0
        mem = {}
        for (i, h) in enumerate(hours):
            presum += 1 if h > 8 else -1
            if presum > 0:
                res = i + 1
            elif presum - 1 in mem:
                res = max(res, i - mem[presum - 1])
            if presum not in mem:
                mem[presum] = i
        return res
