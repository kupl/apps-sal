class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        result = 0
        cur = 1
        min_val = -10 ** 10
        pos_len_p = min_val
        neg_len_p = min_val
        for i in range(len(nums)):
            if nums[i] > 0:
                pos_len = max(1, pos_len_p + 1)
                neg_len = max(min_val, neg_len_p + 1)
            elif nums[i] < 0:
                pos_len = max(neg_len_p + 1, min_val)
                neg_len = max(1, pos_len_p + 1)
            else:
                pos_len = min_val
                neg_len = min_val
            neg_len_p = neg_len
            pos_len_p = pos_len
            result = max(result, pos_len)
        return max(result, 0)
