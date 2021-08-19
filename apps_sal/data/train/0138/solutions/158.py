class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        (pos, neg) = (-1, None)
        (P, Max) = (1, 0)
        for i in range(len(nums)):
            P *= nums[i]
            if P == 0:
                (pos, neg) = (i, None)
                P = 1
            elif P < 0 and neg is None:
                neg = i
            elif P < 0:
                Max = max(Max, i - neg)
            else:
                Max = max(Max, i - pos)
        return Max
