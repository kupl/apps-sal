class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        
        memo = {0: 0, 1: 0}
        cumsum = 0
        
        # Odd + Even = Odd
        # Even + Even = Even
        # Odd + Odd = Even
        
        res = 0
        
        for v in arr:
            cumsum += v
            
            if cumsum % 2 == 0:
                # Is Even
                memo[0] += 1
                res = (res + memo[1]) % MOD
                
            else:
                # Is Odd
                memo[1] += 1
                res = (1 + res + memo[0]) % MOD
                
        return res
