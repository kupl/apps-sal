class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        d = {}
        ct = 0
        M = len(nums1)
        N = len(nums2)

        for i in range(M):
            if(nums1[i] * nums1[i] in d):
                d[nums1[i] * nums1[i]] += 1
            else:
                d[nums1[i] * nums1[i]] = 1

        for i in range(N):
            for j in range(i + 1, N):
                if(nums2[i] * nums2[j] in d):
                    ct += d[nums2[i] * nums2[j]]
        d = {}
        for i in range(N):
            if(nums2[i] * nums2[i] in d):
                d[nums2[i] * nums2[i]] += 1
            else:
                d[nums2[i] * nums2[i]] = 1

        for i in range(M):
            for j in range(i + 1, M):
                if(nums1[i] * nums1[j] in d):
                    ct += d[nums1[i] * nums1[j]]
        return ct
