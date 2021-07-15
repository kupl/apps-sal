class Solution:
    dp = {}
    
    def traverse(self, pos, steps, arrLen):
        key = (pos, steps)
        dp = self.dp
        
        if key not in dp:
            if pos<0 or pos>=arrLen:
                r = 0
            elif pos > steps:
                r = 0
            elif steps == 0:
                if pos == 0:
                    r = 1
                else:
                    r = 0
            else:
                r = (self.traverse(pos-1, steps-1,arrLen)+self.traverse(pos,steps-1,arrLen)+self.traverse(pos+1, steps-1, arrLen))%1000000007
            
            dp[key] = r
        
        return dp[key]
        
    def numWays(self, steps: int, arrLen: int) -> int:
        self.dp={}
        return self.traverse(0, steps, arrLen)
