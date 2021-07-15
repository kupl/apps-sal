class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, target: int) -> int:
        target *= k
        ans = 0
        summ = 0
        for i,n in enumerate(nums):
            if i >= k:
                summ -= nums[i - k]
                
            summ += n
            
            if i >= k - 1:
                if summ >= target:
                    ans += 1
        return ans
