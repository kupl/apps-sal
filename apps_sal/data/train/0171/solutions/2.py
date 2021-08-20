class Solution:

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        ans = nums[0]
        l = 0
        r = n - 1
        prod = 1
        i = 0
        while i < n:
            if nums[i] == 0:
                zero_idx = i
                return max(self.maxProduct(nums[zero_idx + 1:]), max(0, self.maxProduct(nums[0:zero_idx])))
            else:
                prod = prod * nums[i]
                i = i + 1
        if prod > 0:
            return prod
        prod_right = prod
        max_prod_right = prod
        prod_left = prod
        max_prod_left = prod
        if prod < 0:
            while 0 <= r:
                prod_right = prod_right // nums[r]
                r = r - 1
                if prod_right > max_prod_right:
                    if prod_right > 0:
                        max_prod_right = prod_right
                        break
                    else:
                        max_prod_right = prod_right
            print(max_prod_left)
            while l < n:
                prod_left = prod_left // nums[l]
                l = l + 1
                if prod_left > max_prod_left:
                    if prod_left > 0:
                        max_prod_left = prod_left
                        break
                else:
                    max_prod_left = prod_left
        return max(max_prod_left, max_prod_right)
