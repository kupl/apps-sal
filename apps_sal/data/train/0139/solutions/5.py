class Solution:
  def minDeletionSize(self, words: List[str]) -> int:
    n = len( words )
    if n==0:
      return 0
    w = len( words[0] )
    intervals = [[0,n]]
    del_cols = 0
    for col in range(w):
      next_intervals = []
      del_this_col = 0
      for start,end in intervals:
        cprev = words[start][col]
        iprev = start
        for i in range(start+1,end):
          c = words[i][col]
          if c>cprev:
            ## create new interval
            ## reset cprev and iprev
            next_intervals.append( [iprev,i] )
            cprev = c
            iprev = i
          elif c<cprev:
            del_this_col = 1
            del_cols += 1
            break
          pass
        if del_this_col:
          break
        ## add another last interval
        next_intervals.append( [iprev, end] )
        pass
      if not del_this_col:
        intervals = next_intervals
      pass
    return del_cols
