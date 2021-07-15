class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        start = 1
        end = max(nums)
        
        while start <= end:
            mid = (start + end) // 2
            result = self.satistfy(nums, mid)

            if result <= threshold:
                end = mid - 1
            else:
                start = mid + 1

        return start
    
    def satistfy(self, nums, mid):
        return sum(list([math.ceil(x/mid) for x in nums]))
        

