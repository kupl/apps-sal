from functools import lru_cache

class Solution:
  @lru_cache(None)
  def winnerSquareGame(self, n: int) -> bool:
    for i in range(1, n + 1):
      if i * i > n:
        break
      if i * i == n:
        return True
      if not self.winnerSquareGame(n - i * i):
        return True
    return False

