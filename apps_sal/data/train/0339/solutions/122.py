class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        t1 = dict(collections.Counter(nums1))
        t2 = dict(collections.Counter(nums2))
        c = 0
        for j in range(len(nums1)):
            for k in range(j+1, len(nums1)):
                temp = math.sqrt(nums1[j] *nums1[k])
                if temp in t2:
                    c += t2[temp]
        for j in range(len(nums2)):
            for k in range(j+1, len(nums2)):
                temp = math.sqrt(nums2[j] *nums2[k])
                if temp in t1:
                    c += t1[temp]
        return c
