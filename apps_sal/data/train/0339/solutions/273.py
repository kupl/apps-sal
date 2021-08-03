from collections import Counter


class Solution:

    def search(self, nums1, nums2, counter):
        for i in range(len(nums1)):
            if nums1[i] ** 2 > nums2[-1] ** 2:
                break
            for j in range(i + 1, len(nums1)):
                if nums1[i] * nums1[j] > nums2[-1] ** 2:
                    break
                target = nums1[i] * nums1[j]
                self.rst += counter[target]

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        if not nums1 or not nums2:
            return 0
        nums1.sort()
        nums2.sort()
        counter1 = Counter([x**2 for x in nums1])
        counter2 = Counter([x**2 for x in nums2])
        self.rst = 0
        self.search(nums1, nums2, counter2)
        self.search(nums2, nums1, counter1)
        return self.rst
