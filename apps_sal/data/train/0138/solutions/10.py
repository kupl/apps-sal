class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        @lru_cache(None)
        def pos_helper(len):
            if len == 0:
                return 0
            if len == 1:
                return 1 if nums[0] > 0 else 0
            if nums[len - 1] > 0:
                return pos_helper(len - 1) + 1
            if nums[len - 1] == 0:
                return 0
            if nums[len - 1] < 0:
                return neg_helper(len - 1) + 1 if neg_helper(len - 1) != 0 else 0

        @lru_cache(None)
        def neg_helper(len):
            if len == 0:
                return 0
            if len == 1:
                return 1 if nums[0] < 0 else 0
            if nums[len - 1] > 0:
                return neg_helper(len - 1) + 1 if neg_helper(len - 1) > 0 else 0
            if nums[len - 1] == 0:
                return 0
            if nums[len - 1] < 0:
                return pos_helper(len - 1) + 1

        res = 0
        for i in range(0, len(nums) + 1):
            res = max(res, pos_helper(i))
        return res
