#744

M = int(1e9+7)


class Solution:
  def numOfSubarrays(self, arr: List[int]) -> int:
      n = len(arr)
      odd = [-1] * n
      even = [-1] * n
      
      odd[0] = 1 if arr[0] % 2 == 1 else 0
      even[0] = 1 if arr[0] % 2 == 0 else 0
      
      for i in range(1, n):
        v = arr[i]
        if v % 2 == 1:
          odd[i] = (1 + even[i-1]) % M
          even[i] = odd[i-1]
        else:
          odd[i] = odd[i-1]
          even[i] = (even[i-1] + 1) % M
      
      
      ret = 0
      for v in odd:
        ret = (ret + v) % M
      return ret
