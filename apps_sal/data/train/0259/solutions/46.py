class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def feasible(div):
            count = 0
            for num in nums:
                count += (num-1)//div + 1
            return count<=threshold
        
        left = 1
        right = max(nums)
        
        while left < right:
            mid = left + ((right-left)>>1)
            if feasible(mid):
                right = mid
            else:
                left = mid+1
        return left
