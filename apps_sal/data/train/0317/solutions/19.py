class Solution:
    def numPermsDISequence(self, S: str) -> int:
        n = len(S)
        if n <= 1: return 1
        
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        dp[0][0] = 1
        
        for idx, s in enumerate(S):
            for end in range(idx+2):
                if s == 'D':
                    for i in range(end, idx+2):
                        dp[idx+1][end] += dp[idx][i]
                else:
                    for i in range(end):
                        dp[idx+1][end] += dp[idx][i]
                        
        # for d in dp: print(d)
        return sum(dp[-1]) % (10 ** 9 + 7)
