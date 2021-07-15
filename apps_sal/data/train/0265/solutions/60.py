class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
      
        prefix = {0:-1}
        cur = 0
        res = 0
        for i,v in enumerate(nums):  
          cur += v
          if (cur - target) in prefix:
            res += 1
            prefix = {}
            
          prefix[cur] = i

        return res
            
          

