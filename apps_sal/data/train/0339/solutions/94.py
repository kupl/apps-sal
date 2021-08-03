class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        d1 = {}
        d2 = {}
        cnt1, cnt2 = 0, 0
        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                if nums1[i] * nums1[j] not in d1:
                    d1[nums1[i] * nums1[j]] = 1
                else:
                    d1[nums1[i] * nums1[j]] += 1
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                if nums2[i] * nums2[j] not in d2:
                    d2[nums2[i] * nums2[j]] = 1
                else:
                    d2[nums2[i] * nums2[j]] += 1
        for i in range(len(nums1)):
            if nums1[i]**2 in d2:
                cnt1 += d2[nums1[i]**2]
        for i in range(len(nums2)):
            if nums2[i]**2 in d1:
                cnt2 += d1[nums2[i]**2]
        return cnt1 + cnt2
