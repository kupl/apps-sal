class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        seta = {}
        setb = {}
        for i in nums1:
            if i * i in seta:
                seta[i * i] += 1
            else:
                seta[i * i] = 1
        for i in nums2:
            if i * i in setb:
                setb[i * i] += 1
            else:
                setb[i * i] = 1
        ans = 0
        for i in range(len(nums1) - 1):
            for j in range(i + 1, len(nums1)):
                if nums1[i] * nums1[j] in setb:
                    ans += setb[nums1[i] * nums1[j]]
        for i in range(len(nums2) - 1):
            for j in range(i + 1, len(nums2)):
                if nums2[i] * nums2[j] in seta:
                    ans += seta[nums2[i] * nums2[j]]
        return ans
