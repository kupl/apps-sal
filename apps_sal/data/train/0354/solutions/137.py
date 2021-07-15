class Solution:
  def dieSimulator(self, n: int, rollMax: List[int]) -> int:
    # Basic solution: 3 dimensions, n rolls, last roll, last consecutive count -> O(n^2)
    # Can we reduce to O(n) or O(nlogn)? Seems not.
    d = {}
    def dp(n, v, k): # n rolls, last is v, v has at most k consecutive (k > 1. Notice: don't handle k == 0, since it will include others repeated, e.g. k == 0 for 1 includes k == 0 for 2, etc.)
#       if n == 1:
#         return 1 if k == 1 else 0
#       if (n, v, k) not in d:
#         if k == 1:
#           d[(n, v, k)] = 0
#           for i, lim in enumerate(rollMax):
#             if i != v:
#               d[(n, v, k)]
#         else:
#           d[(n, v, k)] = dp(n-1, v, k-1)
      
      if n == 1:
        return 1
      if (n, v, k) not in d:
        if k == 1:
          d[(n, v, k)] = 0
          for i, lim in enumerate(rollMax):
            if i != v:
              d[(n, v, k)] += dp(n-1, i, lim) # All others
        elif k == 2:
          d[(n, v, k)] = dp(n, v, 1) + dp(n-1, v, k-1)
        else:
          # atmost(n, v, k) = atmost(n, v, k-1) + exactly(n, v, k) = atmost(n, v, k-1) + exactly(n-1, v, k-1) = atmost(n, v, k-1) + atmost(n-1, v, k-1) - atmost(n-1, v, k-2)
          d[(n, v, k)] = dp(n, v, k-1) + dp(n-1, v, k-1) - dp(n-1, v, k-2)
      return d[(n, v, k)]
    
    def get_exact(n, v, k):
      if k == 1:
        return dp(n, v, k)
      return dp(n, v, k) - dp(n, v, k-1)
    
    res = 0
    for i, lim in enumerate(rollMax):
      for j in range(1, lim+1):
        res += get_exact(n, i, j)

    return res % (10**9 + 7)
