class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = {}
        total = sum(stoneValue)
        def help(start, s):
            if start in dp: return dp[start]
            if start >= len(stoneValue): return 0
            dp[start] = max(s - help(start+1, s-stoneValue[start]), s- help(start+2,s-sum(stoneValue[start:start+2])), s-help(start+3,s-sum(stoneValue[start: start+3])))
            return dp[start]
        
        
        A = help(0, total)
       
        if 2*A > total: return 'Alice'
        elif 2*A == total: return 'Tie'
        else: return 'Bob'
