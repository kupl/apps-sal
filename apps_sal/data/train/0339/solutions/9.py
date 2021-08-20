class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        l1 = len(nums1)
        l2 = len(nums2)
        upper1 = []
        upper2 = []
        for i in range(l1):
            for j in range(i + 1, l1):
                upper1.append(nums1[i] * nums1[j])
        for i in range(l2):
            for j in range(i + 1, l2):
                upper2.append(nums2[i] * nums2[j])
        Count_upper1 = collections.Counter(upper1)
        Count_upper2 = collections.Counter(upper2)
        count = 0
        for i in range(l1):
            count += Count_upper2[nums1[i] ** 2]
        for i in range(l2):
            count += Count_upper1[nums2[i] ** 2]
        return count
