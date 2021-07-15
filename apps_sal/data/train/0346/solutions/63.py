class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
      odd_pos = [pos for pos, e in enumerate(nums) if e % 2 == 1]

      if len(odd_pos) < k:
        return 0
      
      spaces = []
      prev_pos = -1
      for pos in odd_pos:
        spaces.append(pos - prev_pos)
        prev_pos = pos
      spaces.append(len(nums) - prev_pos)
      
      res = 0
      for i in range(len(spaces) - k):
        res += spaces[i] * spaces[i + k]
        
        
      return res
