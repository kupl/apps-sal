class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        (max_len, start, product, first_minus_index) = (0, 0, 1, -1)
        for (i, n) in enumerate(nums):
            if n == 0:
                (start, product, first_minus_index) = (i + 1, 1, -1)
            else:
                if n < 0 and first_minus_index == -1:
                    first_minus_index = i
                product *= n
                if n > 0:
                    max_len = max(max_len, 1)
                if product > 0:
                    max_len = max(max_len, i - start + 1)
                if product < 0 and first_minus_index != -1:
                    max_len = max(max_len, i - first_minus_index)
        return max_len
