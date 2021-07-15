class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        dic1 = {}
        dic2 = {}
        for i in range(len(nums1)-1):
            for j in range(i+1, len(nums1)):
                v = nums1[i] * nums1[j]
                if dic1.get(v) is None:
                    dic1[v] = 1
                else:
                    dic1[v] = dic1[v]+1
        for i in range(len(nums2)-1):
            for j in range(i+1, len(nums2)):
                v = nums2[i] * nums2[j]
                if dic2.get(v) is None:
                    dic2[v] = 1
                else:
                    dic2[v] = dic2[v]+1
        cnt = 0
        for v in nums1:
            if dic2.get(v*v):
                cnt += dic2.get(v*v)
        for v in nums2:
            if dic1.get(v*v):
                cnt += dic1.get(v*v)
        return cnt

