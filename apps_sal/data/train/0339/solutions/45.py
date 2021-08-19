class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        hash1 = defaultdict(int)
        hash2 = defaultdict(int)
        count = 0
        for i in nums1:
            hash1[i * i] += 1
        for i in nums2:
            hash2[i * i] += 1
        for i in range(len(nums1) - 1):
            for j in range(i + 1, len(nums1)):
                if nums1[i] * nums1[j] in hash2:
                    count += hash2[nums1[i] * nums1[j]]
        for i in range(len(nums2) - 1):
            for j in range(i + 1, len(nums2)):
                if nums2[i] * nums2[j] in hash1:
                    count += hash1[nums2[i] * nums2[j]]
        return count
