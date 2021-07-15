
class Solution:
  def winnerSquareGame(self, n: int) -> bool:
    squart_num = []
    dp = [False] * (n + 1)
    i = 1

    for i in range(1, n + 1):
      start_index = 1
      while True:
        if start_index * start_index > i:
          break
        if not dp[i - start_index * start_index]:
          dp[i] = True
        start_index += 1

        pass
    if dp[n] == 1:
      return True
    return False
    pass

