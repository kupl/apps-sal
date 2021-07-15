class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def enough(x):
            cnt = 0
            for num in nums:
                cnt += int(num//x) + (num%x > 0)
            return cnt <= threshold
        
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if enough(mid):
                right = mid
            else:
                left = mid+1
        return left
