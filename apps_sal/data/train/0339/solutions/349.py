class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        for i in range(len(nums1)):
            hashmap = collections.defaultdict(int)
            for j in range(len(nums2)):
                if nums1[i] * nums1[i] / nums2[j] in hashmap:
                    ans += hashmap[nums1[i] * nums1[i] / nums2[j]]
                hashmap[nums2[j]] += 1
        for i in range(len(nums2)):
            hashmap = collections.defaultdict(int)
            for j in range(len(nums1)):
                if nums2[i] * nums2[i] / nums1[j] in hashmap:
                    ans += hashmap[nums2[i] * nums2[i] / nums1[j]]
                hashmap[nums1[j]] += 1
        return ans
