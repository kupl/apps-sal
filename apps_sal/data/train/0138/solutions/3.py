class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        pos_p = 0
        neg_p = 0
        (pos, neg) = (0, 0)
        result = 0
        for i in range(len(nums)):
            (pos_p, neg_p) = (pos, neg)
            if nums[i] > 0:
                pos = 1 + pos_p
                neg = 1 + neg_p if neg_p > 0 else 0
            elif nums[i] < 0:
                pos = 1 + neg_p if neg_p > 0 else 0
                neg = 1 + pos_p if pos_p > 0 else 1
            else:
                (pos, neg) = (0, 0)
            result = max(result, pos)
        return result
