# Binary Search
import math

class Solution:
    def smallestDivisor(self, nums, threshold):

        nums.sort()
        # you can take hi=10^6 as well
        # but hi=max_element, will also be correct
        # because nums.length <= threshold
        ans = float('+INF')
        lo, hi = 1, nums[-1]
        while lo<=hi:
            mid = lo + (hi-lo)//2
            if self.div(nums, mid) <= threshold:
                ans = min(ans, mid)
                hi = mid-1
            else:
                lo = mid+1
        
        return ans

    def div(self, nums, mid):
        t_sum=0
        for i in nums:
            t_sum += int(math.ceil(i/mid))
        return t_sum



