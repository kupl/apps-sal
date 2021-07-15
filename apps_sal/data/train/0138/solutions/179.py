class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        first_neg = None
        last_neg = None
        first_pos = None
        cum_prod = 1
        max_len = 0
        last_zero_idx = 0
        for idx, val in enumerate(nums):
            if val == 0:
                first_neg = None
                last_neg = None
                first_pos = None
                cum_prod = 1
                last_zero_idx = idx + 1
            else:
                cum_prod *= val
                if cum_prod > 0:
                    max_len = max(max_len, idx - last_zero_idx + 1)
                else:
                    if first_neg is None:
                        first_neg = idx
                    last_neg = idx
                    max_len = max(max_len, last_neg - first_neg)
        return max_len
