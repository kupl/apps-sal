class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
      coinsCount = dict()
      #fill dict:
      for i in range (1, amount+1):
        coinsCount[i] = 9999
      coinsCount[0] = 0
      for i in range(1, amount+1):
        for icoin in range (0, len(coins)):
          curDenom = coins[icoin]
          difference = i - curDenom
          if difference >= 0:
            coinsCount[i] = min(1 + coinsCount[difference], coinsCount[i])
          elif difference == 0:
            coinsCount[i] +=1
      if (coinsCount[amount] != 9999):
        return coinsCount[amount]
      return -1
      

