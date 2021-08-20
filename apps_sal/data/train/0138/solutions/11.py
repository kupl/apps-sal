class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        (pos, neg) = (0, 0)
        if nums[0] > 0:
            pos = 1
        if nums[0] < 0:
            neg = 1
        ans = pos
        for i in range(1, n):
            if nums[i] > 0:
                pos_next = 1 + pos
                neg_next = 1 + neg if neg > 0 else 0
            elif nums[i] < 0:
                pos_next = 1 + neg if neg > 0 else 0
                neg_next = 1 + pos
            else:
                (pos_next, neg_next) = (0, 0)
            (pos, neg) = (pos_next, neg_next)
            ans = max(ans, pos)
        return ans
