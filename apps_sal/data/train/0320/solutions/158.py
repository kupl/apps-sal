class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        
        while True:
            for i in range(n):
                if nums[i] % 2 == 1:
                    ans += 1
                    nums[i] -= 1
                    
            stop = True
            for i in range(n):
                if nums[i] != 0:
                    nums[i] //= 2
                    stop = False
            
            if stop:
                break
            else:
                ans += 1
        return ans

