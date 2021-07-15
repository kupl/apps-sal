class Solution:
    def profitableSchemes(self, G: int, P: int, groups: List[int], profits: List[int]) -> int:
        dp = [[0] * (P+1) for i in range(0,G+1)]
        for i in range(0, G+1):
            dp[i][0] = 1
        N = len(groups)
        l = []
        for i in range(0, N):
            l.append((groups[i], profits[i]))
        l.sort()
        
        for i in range(0, N):
            group, profit = l[i]
            if group > G:
                break
            for j in range(G, group - 1, -1):
                gremain = j - group
                for k in range(P, -1, -1):
                    dp[j][k] += dp[gremain][max(k - profit, 0)]
                    dp[j][k] %= (10**9 + 7)
                
        return dp[G][P]
