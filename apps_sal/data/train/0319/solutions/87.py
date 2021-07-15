class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        total = sum(stoneValue)
        dp = {}
        alice_get = self.find_score(stoneValue, 0, dp)
        if alice_get * 2 > total:
            return 'Alice'
        elif alice_get * 2 < total:
            return 'Bob'
        else:
            return 'Tie'
    
    
    def find_score(self, stoneValue, i, dp):
        if i in dp:
            return dp[i]
        if i == len(stoneValue) - 1:
            return stoneValue[i]
        elif i >= len(stoneValue):
            return 0
        elif i == len(stoneValue) - 2:
            return max(stoneValue[i] + stoneValue[i + 1], stoneValue[i])
        else:
            dp[i] = max(stoneValue[i] + min(self.find_score(stoneValue, i + 2, dp), self.find_score(stoneValue, i + 3, dp),self.find_score(stoneValue, i + 4, dp)),
                        stoneValue[i] + stoneValue[i + 1] + min(self.find_score(stoneValue, i + 5, dp), self.find_score(stoneValue, i + 3, dp),self.find_score(stoneValue, i + 4, dp)),
                        stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] + min(self.find_score(stoneValue, i + 5, dp), self.find_score(stoneValue, i + 6, dp),self.find_score(stoneValue, i + 4, dp))        
            )
            return dp[i]
