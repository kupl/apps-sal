class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        high = math.ceil(max(nums) * len(nums) / threshold)
        low = math.ceil(sum(nums) / threshold)
        while high > low: 
            mid = (high + low) // 2
            tot = 0
            for num in nums:
                tot += math.ceil(num / mid)
            if tot <= threshold: 
                high = mid  
            else: 
                low = mid + 1
        return high

