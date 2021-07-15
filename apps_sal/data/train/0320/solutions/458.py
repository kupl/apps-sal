class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n, res = len(nums), 0
        while True:  
            count, i = 0, 0
            while i < n: 
                if nums[i] % 2: break
                if nums[i] == 0: count += 1
                i += 1
            if count == n: return res  
            if i == n:
                for j in range(n): nums[j] = nums[j] // 2 
                res += 1
            for j in range(i, n):  
                if nums[j] % 2:  
                    nums[j] -= 1 
                    res += 1 
        return res
