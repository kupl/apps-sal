from collections import Counter


class Solution:

    def check_square(self, c, nums):
        tot = 0
        for j in range(len(nums)):
            for k in range(j + 1, len(nums)):
                tot += c[nums[j] * nums[k]]
        return tot

    def count_squares(self, nums):
        c = Counter([elem**2 for elem in nums])
        return c

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        c1 = self.count_squares(nums1)
        c2 = self.count_squares(nums2)

        sol1 = self.check_square(c1, nums2)
        sol2 = self.check_square(c2, nums1)

        return sol1 + sol2
