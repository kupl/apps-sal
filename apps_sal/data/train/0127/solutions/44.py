class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        n = len(profit)
        dp = [[[0 for g in range(G+1)] for p in range(P+1)] for i in range(1+n)]
        # NOTE: here p and g is not \"budget\", but actual value, to avoid duplication!
        
        # initialization: i = 0
        dp[0][0][0] = 1

        
        # fill the restL i > 0
        for i in range(1, n+1):
            for p in range(P+1):
                for g in range(G+1):
                    # ending at ith crime with p profit lower limit and g group members upper limit
                    dp[i][p][g] = dp[i-1][p][g] # commit or not commit ith crime
                    if g >= group[i-1]:
                        dp[i][p][g] += dp[i-1][max(p-profit[i-1], 0)][g-group[i-1]]

        result = 0
        for value in dp[n][P][:G+1]:
            result += value
        return result % (10**9 + 7)
