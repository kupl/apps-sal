class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cur_pos_product_len = 1 if nums[0] > 0 else 0
        cur_neg_product_len = 1 if nums[0] < 0 else 0
        max_len = cur_pos_product_len
        for i in range(1, len(nums)):
            if nums[i] > 0:
                cur_pos_product_len += 1
                cur_neg_product_len = cur_neg_product_len + 1 if cur_neg_product_len > 0 else 0
            elif nums[i] < 0:
                temp = cur_pos_product_len
                cur_pos_product_len = cur_neg_product_len + 1 if cur_neg_product_len > 0 else 0
                cur_neg_product_len = temp + 1
            else:
                cur_pos_product_len = 0
                cur_neg_product_len = 0
            max_len = max(max_len, cur_pos_product_len)
        return max_len
