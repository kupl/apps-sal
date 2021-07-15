class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prev, _next, n = [0 for _ in range(len(nums))], [0 for _ in range(len(nums))], len(nums)
        
        count = 0
        for i in range(n):
            num = nums[i]
            if i == 0:
                if num:
                    count = 1
            else:
                if num:
                    prev[i] = count 
                    count += 1
                else:
                    prev[i] = count
                    count = 0
        
        count = 0
        for i in range(n-1, -1, -1):
            num = nums[i]
            if i == n - 1:
                if num:
                    count = 1
            else:
                if num:
                    _next[i] = count 
                    count += 1
                else:
                    _next[i] = count
                    count = 0
        
        _max = 0
        
        for i in range(n):
            num = nums[i]
            _max = max(_max, prev[i] + _next[i])
        
        return _max
