from collections import defaultdict


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        product_set1, product_set2 = defaultdict(int), defaultdict(int)
        numss = [nums1, nums2]
        for n in range(2):
            if n == 0:
                s = product_set1
            else:
                s = product_set2
            nums = numss[n]
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    s[nums[i] * nums[j]] += 1

        ans = 0
        for n in range(2):
            if n == 0:
                s = product_set2
            else:
                s = product_set1
            nums = numss[n]
            for i in range(len(nums)):
                ans += s[nums[i] * nums[i]]
        return ans
