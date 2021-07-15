class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        s = sum(nums)
        lo = max(1, s // threshold)
        hi = max(nums)
        
        while lo < hi:
            mid = (lo + hi) // 2
            r = sum([math.ceil(n / mid) for n in nums])
            if r > threshold:
                lo = mid + 1
            else:
                hi = mid
                
        return lo
