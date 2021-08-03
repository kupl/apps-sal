class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        ct = 0
        d = {}
        for j in range(len(nums2)):
            for k in range(j + 1, len(nums2)):
                if nums2[j] * nums2[k] in d:
                    d[nums2[j] * nums2[k]] = d[nums2[j] * nums2[k]] + 1
                else:
                    d[nums2[j] * nums2[k]] = 1
        dd = {}
        for j in range(len(nums1)):
            for k in range(j + 1, len(nums1)):
                if nums1[j] * nums1[k] in dd:
                    dd[nums1[j] * nums1[k]] = dd[nums1[j] * nums1[k]] + 1
                else:
                    dd[nums1[j] * nums1[k]] = 1

        ct = 0
        for i in range(len(nums1)):
            x = nums1[i] * nums1[i]
            if x in d:
                ct = ct + d[x]

        for i in range(len(nums2)):
            x = nums2[i] * nums2[i]
            if x in dd:
                ct = ct + dd[x]
        return ct
