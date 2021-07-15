class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        leftones = [0] * n
        for i in range(n):
            if nums[i] == 0: leftones[i] = 0
            else: leftones[i] = 1 if i == 0 else leftones[i-1]+1
                
        rightones = [0] * n
        for i in range(n-1, -1, -1):
            if nums[i] == 0: rightones[i] = 0
            else: rightones[i] = 1 if i == n-1 else rightones[i+1]+1
                
        res = 0
        for i in range(1, n-1):
            res = max(res, leftones[i-1] + rightones[i+1])
        
        return res

