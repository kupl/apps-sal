class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
      winner = float('inf')
      wins = 0
      backup = max(arr)
      runs = 0
      shortcircuit = len(arr)
      
      while winner == float('inf'):
        runs += 1
        if runs >= shortcircuit:
          return backup
        
        if arr[0] > arr[1]:
          arr.append(arr[1])
          del arr[1]
          wins += 1
        else:
          arr.append(arr[0])
          del arr[0]
          wins = 1
          
        if wins >= k:
          winner = arr[0]
      
      return winner

