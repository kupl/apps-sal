class Solution:
    def __init__(self):
        self.dp = [] 
        
    def utility(self, n, rollMax, lastVal, count):
        if n == 0:
            return 1
        
        if self.dp[n][lastVal][count] is not None:
            return self.dp[n][lastVal][count]
        
        ans=0
        for i in range(1, 7):
            if lastVal == i:
                if rollMax[lastVal-1] > count:
                    ans += self.utility(n-1, rollMax, lastVal, count+1)
                else:
                    continue
            else:
                ans += self.utility(n-1, rollMax, i, 1) 

            
        self.dp[n][lastVal][count] = ans % 1000000007

        return self.dp[n][lastVal][count]
        
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        self.dp = [[[None for i in range(16)] for j in range(7)] for k in range(5001)]
        return self.utility(n, rollMax, -1, 0)
