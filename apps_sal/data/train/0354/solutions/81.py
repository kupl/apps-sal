class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        modulo = 10**9 + 7
        dp = [[0 for _ in range(6)] for _ in range(n)]
        
        for roll in range(n):
            for number in range(6):
                for limit in range(1, rollMax[number]+1):
                    if roll >= limit:
                        for possibility in range(6):
                            if possibility != number:
                                dp[roll][number] = (dp[roll][number] + dp[roll-limit][possibility])%modulo
                    else:
                        dp[roll][number] += 1
                        break
                
    
        return sum(dp[n-1])%modulo
