from collections import Counter
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n1_cnts, n2_cnts = Counter(nums1), Counter(nums2)
        
        good = 0
        n2_cnts_copy = n2_cnts.copy()
        for n2j in nums2:
            n2_cnts_copy[n2j] -= 1
            for n1, cnt in list(n1_cnts.items()):
                good += cnt*n2_cnts_copy[n1**2/n2j]
                
        for n1j in nums1:
            n1_cnts[n1j] -= 1
            for n2, cnt in list(n2_cnts.items()):
                good += cnt*n1_cnts[n2**2/n1j]
                
        return good
        

