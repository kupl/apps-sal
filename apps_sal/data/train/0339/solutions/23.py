class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        import numpy as np
        l1 = len(nums1)
        l2 = len(nums2)
        upper1 = list(np.outer(np.array(nums1), np.array(nums1))[np.triu_indices(l1, 1)])
        upper2 = list(np.outer(np.array(nums2), np.array(nums2))[np.triu_indices(l2, 1)])
        Count_upper1 = collections.Counter(upper1)
        Count_upper2 = collections.Counter(upper2)
        count = 0
        for i in range(max(l1, l2)):
            if i < l1:
                count += Count_upper2[nums1[i] ** 2]
            if i < l2:
                count += Count_upper1[nums2[i] ** 2]
        return count
