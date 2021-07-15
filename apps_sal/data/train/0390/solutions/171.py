import functools
import math


class Solution:
  def winnerSquareGame(self, n: int) -> bool:
    @functools.lru_cache(None)
    def dp(k):
      if k <= 0:
        return False

      sq = math.sqrt(k)
      if sq.is_integer():
        return True

      for m in range(1, k):
        if m ** 2 > k:
          break

        ans = dp(k - m ** 2)
        if not ans:
          return True

      return False

    return dp(n)
