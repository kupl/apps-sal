#import math
from numpy import ceil
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def candidate(val):
            #res = sum(math.ceil(v/val) for v in nums)
            res = sum((v-1)//val + 1 for v in nums)
            return res <= threshold
        
        lo, hi = 1, max(nums)
        while lo < hi:
            med = lo + (hi-lo)//2
            if candidate(med):
                hi = med
            else:
                lo = med+1
        return hi
