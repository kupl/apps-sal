class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def twoProduct(arr, target):
            # returns the count of pairs in arr whose product equals target
            # twoProduct([2,3,1,3,4,6], 6) => 3
            d = {}
            ret = 0
            for x in arr:
                if target % x == 0 and target // x in d:
                    ret += d[target // x]
                if x in d:
                    d[x] += 1
                else:
                    d[x] = 1
            return ret

        ret = 0
        for x in nums1:
            sq = x**2
            ret += twoProduct(nums2, sq)
        for x in nums2:
            sq = x**2
            ret += twoProduct(nums1, sq)
        return ret
