class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        ret = 0
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)

        for j in range(len(nums2)):
            for k in range(j + 1, len(nums2)):
                dict2[nums2[j] * nums2[k]] += 1

        for j in range(len(nums1)):
            for k in range(j + 1, len(nums1)):
                dict1[nums1[j] * nums1[k]] += 1

        for i in range(len(nums1)):
            if nums1[i]**2 in dict2:
                ret += dict2[nums1[i]**2]

        for i in range(len(nums2)):
            if nums2[i]**2 in dict1:
                ret += dict1[nums2[i]**2]
        return ret
