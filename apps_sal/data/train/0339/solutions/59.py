class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def h(nums1, nums2):
            n = len(nums1)
            counter = collections.Counter()
            for i in range(n):
                for j in range(i + 1, n):
                    counter[nums1[i] * nums1[j]] += 1
            return sum(counter[i**2] for i in nums2)
        return h(nums1, nums2) + h(nums2, nums1)
