class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        def get_code_len(x):
            if x == 1: return 1
            return len(str(x)) + 1 if x >= 2 else 0
        
        n = len(s)
        dp = [ [n] * (k + 1) for _ in range(len(s) + 1)]
        dp[0] = [ 0 ] * (k + 1)
        for i in range(n):
            for j in range( k + 1):
                if j > 0:
                    dp[i + 1][j - 1] = min(dp[i][j], dp[i + 1][j - 1])
                
                deleted = 0
                for p in reversed(list(range(i + 1))):
                    # delete different 
                    if s[i] != s[p]:
                        deleted += 1
                    if deleted > j:
                        break
                    dp[i + 1][j - deleted] = min(
                        dp[i + 1][j - deleted], 
                        dp[p][j] + get_code_len( i + 1 - p - deleted))
        return min(dp[n])

