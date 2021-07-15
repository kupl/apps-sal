class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        MOD = int(1e9 + 7)
        res = even = odd = 0 
        for i, a in enumerate(arr):
            even += 1
            if a % 2 == 1:
                even, odd = odd, even
            res = (res + odd) % MOD
        
        return res 
                

