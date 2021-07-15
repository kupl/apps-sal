class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
      #dpdp
      grid = [0]*len(arr)
      for i in range(len(arr)-1, -1, -1):
        if len(arr) - i <= k:
          grid[i] = max(arr[i:len(arr)])*(len(arr)-i)
        else:
          maxi = 0
          for t in range(k):
            maxi = max(maxi, max(arr[i:i+t+1])*(t+1) + grid[i+t+1])
          grid[i] = maxi
      return grid[0]

