class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        (pos, neg) = (0, 0)
        asr = 0
        for num in nums:
            if num == 0:
                (pos, neg) = (0, 0)
            elif num > 0:
                pos += 1
                neg = neg + 1 if neg else 0
            else:
                n_pos = neg + 1 if neg else 0
                n_neg = pos + 1 if pos else 1
                (pos, neg) = (n_pos, n_neg)
            asr = max(asr, pos)
        return asr
