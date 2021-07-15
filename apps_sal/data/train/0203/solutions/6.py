class Solution:
     def __init__(self):
         self.dp = [[0 for _ in range(101)] for _ in range(101)]
     def go(self, x, y, m, n):
         if self.dp[x][y] == 0:
             if x == m or y == n:
                 self.dp[x][y] = 0
             elif x == m - 1 and y == n - 1:
                 self.dp[x][y] = 1
             elif x == m - 1 and y == n-1:
                 self.dp[x][y] = 1
             else:
                 self.dp[x][y] = self.go(x+1, y, m, n) + self.go(x, y+1, m, n)
         return self.dp[x][y]
     def uniquePaths(self, m, n):
         """
         :type m: int
         :type n: int
         :rtype: int
         """
         return self.go(0, 0, m, n)

