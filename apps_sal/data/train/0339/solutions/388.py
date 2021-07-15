class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        sq1 = collections.Counter([nums1[i] * nums1[j] for i in range(len(nums1)) for j in range(i)])
        sq2 = collections.Counter([nums2[i] * nums2[j] for i in range(len(nums2)) for j in range(i)])
        return sum(sq1[n**2] for n in nums2) + sum(sq2[n**2] for n in nums1)
