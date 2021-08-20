class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        if not nums:
            return 0
        last_neg_i = -1
        acc_product = 1
        bound = -1
        max_len = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                acc_product = 1
                last_neg_i = -1
                bound = i
                continue
            acc_product = acc_product * nums[i]
            if last_neg_i == -1 and acc_product < 0:
                last_neg_i = i
            if acc_product < 0:
                max_len = max(max_len, i - last_neg_i)
            else:
                max_len = max(max_len, i - bound)
        return max_len
