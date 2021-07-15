class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        c1 = collections.Counter([i*i for i in nums1])
        c2 = collections.Counter([i*i for i in nums2])
        res = 0
        for i in range(len(nums1)):
            for j in range(i+1,len(nums1)):
                res += c2[nums1[i]*nums1[j]]
        for i in range(len(nums2)):
            for j in range(i+1,len(nums2)):
                res += c1[nums2[i]*nums2[j]]
        return res
