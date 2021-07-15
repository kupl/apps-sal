MOD = int(1e9 + 7)

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        dp = [-1 for _ in s]
        n = len(s)
        
        def recurse(i: int) -> int:
            if i == n:
                return 1
            
            if dp[i] != -1:
                return dp[i]
            
            result = 0
            val = 0
            for j in range(i, n):
                val = 10 * val + (ord(s[j]) - ord('0'))
                if val > k:
                    break
                elif j == n - 1 or s[j + 1] != '0':
                    result = (result + recurse(j + 1)) % MOD
            dp[i] = result
            return result
        
        return recurse(0)
                
    


