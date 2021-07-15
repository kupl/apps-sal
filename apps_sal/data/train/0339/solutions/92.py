from collections import defaultdict
class Solution:
    
    def getNumOfMatch(self,square,nums):
        res = 0
        h = defaultdict(int)
        n = len(nums)
        for v in nums:
            if square % v == 0:
                res += h[square//v]
                h[v] += 1
        return res
        
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        
        for num in nums1:
            res += self.getNumOfMatch(num*num,nums2)
        for num in nums2:
            res += self.getNumOfMatch(num*num,nums1)
        
        return res
