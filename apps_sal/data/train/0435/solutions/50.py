class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        
        res = 0
        lookup = {0:1}
        presum = 0
        for i, num in enumerate(A):
            presum += num
            remainder = presum % K
            res += lookup.get(remainder, 0)
            lookup[remainder] = lookup.get(remainder, 0) + 1
            
            
        return res

