class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        dp = {}
        MOD = 10**9 + 7
        
        def helper(pre, n0):
            
            if (pre, n0) in dp:
                return dp[(pre, n0)]
            
            if n0 == 0:
                return 1
            
            if pre == 'a':
                subAns = helper('e', n0-1)
            elif pre == 'e':
                subAns = helper('a', n0-1) + helper('i', n0-1)
            elif pre == 'i':
                subAns = helper('a', n0-1) +helper('e', n0-1) + helper('o', n0-1) + helper('u', n0-1)
            elif pre == 'o':
                subAns = helper('i', n0-1) + helper('u', n0-1)
            else:
                subAns = helper('a', n0-1)
                
            dp[(pre, n0)] = subAns%MOD
            
            return subAns
        
        return (helper('a', n-1) +helper('e', n-1) + helper('i', n-1) + helper('o', n-1) + helper('u', n-1))%MOD
