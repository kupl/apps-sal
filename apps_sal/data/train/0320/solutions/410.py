class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        result = 0
        n = len(nums)
        
        while True:
            
            zcount = 0
            
            i = 0
            while i < n:
                if nums[i] % 2 == 1:
                    break
                elif nums[i] == 0:
                    zcount = zcount + 1
                i = i + 1
            
            if zcount == n:
                return result
            
            if i == n:
                for j in range (0, n):
                    nums[j] = nums[j] // 2
                result = result + 1
            
            for j in range (i, n):
                if nums[j] % 2 == 1:
                    nums[j] = nums[j] - 1
                    result = result + 1
            
        return result
