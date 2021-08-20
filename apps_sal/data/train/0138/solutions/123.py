class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        pos = 0
        neg = 0
        res = 0
        for num in nums:
            if num == 0:
                (pos, neg) = (0, 0)
                continue
            elif num > 0:
                if neg > 0:
                    new_neg = neg + 1
                else:
                    new_neg = 0
                new_pos = pos + 1
            elif num < 0:
                if pos > 0:
                    new_neg = pos + 1
                else:
                    new_neg = 1
                if neg > 0:
                    new_pos = neg + 1
                else:
                    new_pos = 0
            (pos, neg) = (new_pos, new_neg)
            res = max(res, pos)
        return res
