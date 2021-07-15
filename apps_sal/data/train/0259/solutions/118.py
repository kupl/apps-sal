class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def feasible(target):
            total = sum([math.ceil(num/target) for num in nums] )
            return total <= threshold
        low,high=1,sum(nums)
        while low < high:
            mid = low+(high-low)//2
            if feasible(mid):
                high = mid
            else:
                low = mid+1
        return low
            

