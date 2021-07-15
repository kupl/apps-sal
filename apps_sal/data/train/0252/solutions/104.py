class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [n for _ in range(n+1)]
        for index,ranged in enumerate(ranges):
            start = max(0,index - ranged)
            end = min(n,index + ranged)
            if start == 0:
                extra = 0
            else:
                extra = dp[start]
            for i in range(start+1,end+1):
                dp[i]= min(dp[i],1 + extra) 
        if dp[-1]!=n:
            return dp[-1]
        else:
            return -1
        

