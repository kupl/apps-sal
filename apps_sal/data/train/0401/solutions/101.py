class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(index, remainder):
            if index == len(nums):
                if remainder == 0:
                    return 0
                else:
                    return -float('inf')
            
            
            new_remainder = (nums[index] + remainder) % 3
            choose = dfs(index + 1, new_remainder) + nums[index]
            no_choose = dfs(index + 1, remainder)
            
            return max(choose, no_choose)
        
        return dfs(0,0)
