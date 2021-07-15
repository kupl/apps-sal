class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        # dp[i][j][k]
        dp = [[[0 for _ in range(16)] for _ in range(6)] for _ in range(n + 1)]
        
        # dp[i][j][k] = The number of sequences with i rolls when the current roll is j and we've rolled j exactly k consecutive times.
        
        for i in range(0, 6):
            dp[1][i][1] = 1
        
        for i in range(2, n + 1):
            for j in range(0, 6):
                for k in range(1, rollMax[j] + 1):
                    if k > i:
                        continue
                    
                    if k == 1:
                        # The previous roll must have been different.
                        for l in range(0, 6):
                            if l == j:
                                continue
                            s = int(sum(dp[i - 1][l]) % (1e9 + 7))
                            dp[i][j][k] += s
                    else:
                        # The previous roll must have been the same.
                        dp[i][j][k] += dp[i - 1][j][k - 1]
                        
                    
        ans = 0
        for arr in dp[n]:
            ans = ans + sum(arr)
        return int(ans % (1e9 + 7))
