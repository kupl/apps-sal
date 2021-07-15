class Solution:
  def getWinner(self, arr: List[int], k: int) -> int:
    wins = 0
    c = 1
    while wins < k and wins < 2*2*len(arr):
      if arr[0] > arr[c]:
        wins += 1
      else:
        arr[0], arr[c] = arr[c], arr[0]
        wins = 1
      c = (c+1) % len(arr)
      if c == 0:
        c += 1
    return arr[0]

