class Solution:

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return None
        (l, r) = (0, n)
        while l + 1 < r:
            mid = l + r >> 1
            if nums[mid] == nums[l]:
                for i in range(l + 1, mid):
                    if nums[i] < nums[l]:
                        r = mid
                        break
                if r != mid:
                    l = mid
            elif nums[mid] > nums[l]:
                l = mid
            else:
                r = mid
        return nums[r % n]
