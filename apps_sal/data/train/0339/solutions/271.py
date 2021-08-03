class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        dic1 = {}
        dic2 = {}
        s1 = []
        s2 = []
        r = 0
        n1 = len(nums1)
        n2 = len(nums2)
        for i in range(n1):
            r += self.helper(nums1[i] * nums1[i], nums2)
        for i in range(n2):
            r += self.helper(nums2[i] * nums2[i], nums1)

        return r

    def helper(self, prod, arr):
        d = {}
        r = 0
        for i in range(len(arr)):
            if prod % arr[i] == 0:
                if prod // arr[i] in d:
                    r += d[prod // arr[i]]
            d[arr[i]] = d.get(arr[i], 0) + 1
        return r
