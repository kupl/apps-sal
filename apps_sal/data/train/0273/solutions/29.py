class Solution:
  def __init__(self):
    self.dp = {0: 0}
  
  def racecar(self, t: int) -> int:
    if t in self.dp:
      return self.dp[t]
    n = t.bit_length()
    if 2**n - 1 == t:
      self.dp[t] = n
    else:
      # go pass via n A's, then turn back
      self.dp[t] = self.racecar(2**n - 1 - t) + n + 1
      # stop after (n - 1) A's, turn back, go m A's, then turn back
      for m in range(n - 1):
        self.dp[t] = min(self.dp[t], self.racecar(t - 2**(n - 1) + 2**m) + n + m + 1)
    return self.dp[t]
