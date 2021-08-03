class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = -float("inf")
        product = 1
        for num in nums:
            product *= num
            max_val = max(product, max_val)
            if num == 0:
                product = 1
        product = 1
        for num in nums[::-1]:
            product *= num
            max_val = max(product, max_val)
            if num == 0:
                product = 1
        return max_val
