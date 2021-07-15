class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        max_div = [0]
        res = 0
        for i in range(n):
            count = 0
            while nums[i] > 0:
                if nums[i] % 2:
                    nums[i] -= 1
                    res += 1
                else:
                    nums[i] /= 2
                    count += 1
                max_div.append(count)
        return res + max(max_div)
            
                    
                
           
            

