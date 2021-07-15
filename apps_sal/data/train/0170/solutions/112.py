# 1040

class Solution:
  def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
    n = len(arr)
    left_good = [True,]
    right_good = [True,]
    for i in range(1, n):
      if arr[i] >= arr[i-1]:
        left_good.append(True)
      else:
        break
        
    left_good.extend([False] * (n - len(left_good)))

    for i in range(n-2, -1, -1):
      if arr[i] <= arr[i+1]:
        right_good.append(True)
      else:
        break
        
    right_good.extend([False] * (n - len(right_good)))
    right_good.reverse()
    
    high = n
    low = 0
    
    def enough(sz):
      if sz == n:
        return True
      if sz == 0:
        return left_good[n-1]
      for begin in range(n):
        end = begin + sz - 1
        if end >= n:
          return False
        a = begin - 1
        b = end + 1
        if (a < 0 or left_good[a]) and (b == n or right_good[b]) and ((not 0 <= a < b < n) or (arr[a] <= arr[b])):
          #print('found ', begin, sz)
          return True
        
      return False
    
    #print(left_good, right_good)
    
    while low <= high:
      cur = int((low + high) / 2) # low + (high - low) / 2
      #print('trying', cur, enough(cur), low, high)
      if enough(cur):
        high = cur - 1
      else:
        low = cur + 1
    
    return low
