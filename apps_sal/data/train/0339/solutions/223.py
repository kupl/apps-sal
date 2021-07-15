import itertools, math
from collections import Counter

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        
        def is_perfect_square(n):
            return int(math.sqrt(n) + 0.5) ** 2 == n
        
        nums1_cntr, nums2_cntr = Counter(nums1), Counter(nums2)
        
        s = 0
        for x, y in itertools.combinations(nums2, 2):
            if is_perfect_square(x * y):
                s += nums1_cntr[math.sqrt(x * y)]
                
        for x, y in itertools.combinations(nums1, 2):
            if is_perfect_square(x * y):
                s += nums2_cntr[math.sqrt(x * y)]
                
        return s
    
                

