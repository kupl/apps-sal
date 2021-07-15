class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        d1 = collections.defaultdict(int)
        d2 = collections.defaultdict(int)
        
        for v in nums1:
            d1[v * v] += 1
        for v in nums2:
            d2[v * v] += 1
            
        for i in range(len(nums2) - 1):
            for j in range(i + 1, len(nums2)):
                if  nums2[i] * nums2[j] in d1:
                    res += d1[nums2[i] * nums2[j]]

        for i in range(len(nums1) - 1):
            for j in range(i + 1, len(nums1)):
                if nums1[i] * nums1[j] in d2:
                    res += d2[nums1[i] * nums1[j]]
        return res

