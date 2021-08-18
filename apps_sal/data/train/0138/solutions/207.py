class Solution:
    def getMaxLen(self, nums: List[int]) -> int:

        carry_len = 0
        left_neg = 0
        max_len = 0
        str_ptr = -1
        for idx, n in enumerate(nums):
            if n < 0:
                left_neg += 1
            carry_len += 1
            if n == 0:
                max_len = max(max_len, 0)
                carry_len = 0
                left_neg = 0
            else:
                max_len = max(max_len, 1 if n > 0 else 0, idx - str_ptr - 1, carry_len if left_neg % 2 == 0 else 0)
            if left_neg == 0:
                str_ptr = idx

        return max_len
