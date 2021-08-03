class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        start, first_neg = -1, float('inf')
        maxi, positive = 0, 1
        for index, value in enumerate(nums):
            if value == 0:
                start, first_neg, positive = index, float('inf'), 1
            else:
                positive = positive == (value > 0)
                if positive:
                    maxi = max(maxi, index - start)
                else:
                    maxi = max(maxi, index - first_neg)
                    first_neg = min(first_neg, index)

        return maxi
