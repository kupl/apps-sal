class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        hashmap1 = {}
        hashmap2 = {}
        count = 0
        for i in range(len(nums1)):
            if nums1[i] * nums1[i] not in hashmap1:
                hashmap1[nums1[i] * nums1[i]] = 1
            else:
                hashmap1[nums1[i] * nums1[i]] += 1
        for j in range(len(nums2)):
            if nums2[j] * nums2[j] not in hashmap2:
                hashmap2[nums2[j] * nums2[j]] = 1
            else:
                hashmap2[nums2[j] * nums2[j]] += 1
        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                if nums1[i] * nums1[j] in hashmap2:
                    count += hashmap2[nums1[i] * nums1[j]]
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                if nums2[i] * nums2[j] in hashmap1:
                    count += hashmap1[nums2[i] * nums2[j]]
        return count
