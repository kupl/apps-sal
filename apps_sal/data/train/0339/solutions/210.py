class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        prod1 = {}
        for i in range(len(nums1) - 1):
            for j in range(i + 1, len(nums1)):
                if nums1[i] * nums1[j] not in prod1.keys():
                    prod1[nums1[i] * nums1[j]] = 1
                else:
                    prod1[nums1[i] * nums1[j]] += 1
        prod2 = {}
        for i in range(len(nums2) - 1):
            for j in range(i + 1, len(nums2)):
                if nums2[i] * nums2[j] not in prod2.keys():
                    prod2[nums2[i] * nums2[j]] = 1
                else:
                    prod2[nums2[i] * nums2[j]] += 1

        cnt = 0
        for i in nums1:
            if i * i in prod2.keys():
                cnt += prod2[i * i]

        for i in nums2:
            if i * i in prod1.keys():
                cnt += prod1[i * i]

        return cnt
