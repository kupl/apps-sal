class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        N = 10**9+7
        
        counts = Counter([num for num in nums if num < target])        
        nums = sorted(list(counts.keys()))
        total = sum(counts.values())
        ans = 0
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left] + nums[right] <= target:
                a = counts[nums[left]]
                total -= a
                ans = (ans + ((1<<a)-1)*(1<<total)) % N
                left += 1
            else:
                total -= counts[nums[right]]
                right -= 1

        return ans
                
        
        
        

