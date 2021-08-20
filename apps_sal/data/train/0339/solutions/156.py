class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        fin = 0
        for i in range(len(nums1)):
            res = 0
            fin += self.finder(nums1[i], nums2, res)
        for i in range(len(nums2)):
            res = 0
            fin += self.finder(nums2[i], nums1, res)
        return fin

    def finder(self, square, arr, res):
        res = 0
        n = square * square
        di = {}
        for i in range(len(arr)):
            if n % arr[i] == 0:
                p = n // arr[i]
                if arr[i] in di:
                    res += di[arr[i]]
                if p in di:
                    di[p] += 1
                else:
                    di[p] = 1
        return res
