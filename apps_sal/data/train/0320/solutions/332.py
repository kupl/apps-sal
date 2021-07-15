class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        ans = 0 
        peak = 0 
        for n in nums :
            ans += bin(n)[2:].count('1')
            peak = max(peak,len(bin(n)[2:])-1)
        return ans + peak 
            

