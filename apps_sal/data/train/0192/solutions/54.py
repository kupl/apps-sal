
class Solution:
  def maxCoins(self, piles: List[int]) -> int:
    result = 0
    piles.sort(reverse= True)

    index = 1
    counter = 0
    while counter < len(piles) // 3:
      result += piles[index]
      index += 2
      counter += 1

    return result
