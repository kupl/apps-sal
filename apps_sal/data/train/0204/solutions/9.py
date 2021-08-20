class Solution:

    def search(self, nums, target):
        if len(nums) <= 3:
            return nums.index(target) if target in nums else -1
        (l, r) = (0, len(nums) - 1)
        while l < r:
            m = (l + r) // 2
            left = nums[l]
            mid = nums[m]
            right = nums[r]
            if left == target:
                return l
            if mid == target:
                return m
            if right == target:
                return r
            elif left < right:
                print(('mono:', l, r))
                if mid < target:
                    l = m
                    r -= 1
                else:
                    r = m
                    l += 1
            else:
                print(('not mono:', l, r))
                if left < target < mid or mid < left < target or target < mid < left:
                    r = m
                    l += 1
                else:
                    l = m
                    r -= 1
        return -1
