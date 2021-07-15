class Solution:
    def __init__(self):
      self.dp = {}
    def dfs(self, i, count):
      if count >= 110:
        return 99999;
      if i in self.dp:
        return self.dp[i]
      tmp = 90
      if i%3 == 0 : tmp = min(tmp, self.dfs(i//3, count + 1))
      if tmp < 100 and i%2 == 0 : tmp = min(tmp, self.dfs(i//2 , count + 1))
      
      if tmp < 100 : tmp = min(tmp, self.dfs(i - 1, count + 1))
      self.dp[i] = 1 + tmp
      return self.dp[i]
    def minDays(self, n: int) -> int:
      self.dp[0] = 0
      self.dp[1] = 1
      self.dp[2] = 2
      self.dp[3] = 2
      self.dp[4] = 3
      return self.dfs(n, 0)
