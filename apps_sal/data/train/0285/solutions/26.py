class Solution:
  def smallestRangeII(self, A: List[int], k: int) -> int:
    A.sort()
    
    res, n = A[-1] - A[0], len(A)
    temp = [max(A[n - 1] - k, A[n - i - 2] + k) - min(A[0] + k, A[n - i - 1] - k) for i in range(n)]
    return min(res, min(temp))
