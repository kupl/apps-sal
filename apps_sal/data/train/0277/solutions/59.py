class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
      res = 0
      grid = [0]*len(light)
      dicts = {}
      for turn in light:
        if turn == 1:
          grid[turn-1] = 1
          start = turn - 1
          while start < len(light):
            if grid[start] != 0:
              if start in dicts: del dicts[start]
              grid[start] = 1
              start += 1
            else:
              break
          if not dicts: res += 1
        else:
          if grid[turn - 2] == 1:
            grid[turn - 1] = 1
            start = turn - 1
            breaked = False
            while start < len(light):
              if grid[start] != 0:
                if start in dicts: del dicts[start]
                grid[start] = 1
                start += 1
              else:
                break
            if not dicts: res += 1           
          else:
            grid[turn -1] = 2
            dicts[turn - 1] = 1
      return res
            
            
        

