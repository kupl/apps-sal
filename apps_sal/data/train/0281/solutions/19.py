from collections import defaultdict

class Solution:
  def canConvertString(self, s: str, t: str, n: int) -> bool:
    if len(s) != len(t):
      return False
    
    d = defaultdict(int)
    for c1, c2 in zip(s, t):
      v = (26 + ord(c2) - ord(c1)) % 26
      if v:
        d[v] += 1
        
    
    for k, v in list(d.items()):
      if k + 26 * (v - 1) > n:
        return False
    
    return True
        

