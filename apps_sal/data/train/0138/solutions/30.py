class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        neg = pos = res = 0
        for n in nums:
            if n == 0:
                neg = pos = 0
            elif n > 0:
                if neg:
                    neg += 1
                pos += 1
            else:
                pos, neg = neg + 1 if neg else 0, pos + 1
            res = max(res, pos)
        return res
