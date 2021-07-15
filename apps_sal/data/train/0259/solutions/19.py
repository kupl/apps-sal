class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        lo, hi = 1, max(nums)
        
        while lo <= hi:
            mid = (lo+hi)//2
            divisor_sum = sum([math.ceil(x/mid) for x in nums]) # will be larger
            next_sum = sum([math.ceil(x/(mid+1)) for x in nums]) # will be smaller
            
            if  next_sum <= threshold < divisor_sum:
                return mid+1
            elif next_sum > threshold:
                lo = mid + 1
            elif divisor_sum <= threshold:
                hi = mid - 1
        
        return 1
