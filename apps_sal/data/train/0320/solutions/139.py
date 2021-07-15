class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        res = 0
        max_len = 0
        for num in nums:
            bits = 0
            while num > 0:
                res += num%2
                num >>= 1
                bits += 1
            max_len = max(bits-1, max_len)
        return res + max_len
            
            
                

