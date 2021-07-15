class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        res = 0
        
        curr_sum = 0
        even_count = 1
        odd_count = 0
        
        for num in arr:
            curr_sum += num
            curr_sum %=2
            
            if curr_sum == 1: # odd
                res += even_count
                odd_count += 1
            else:
                res += odd_count
                even_count += 1
        
        return res % MOD
            
            
            

