class Solution:
  def maximumSum(self, arr: List[int]) -> int:
    max0, max1, result = arr[0], arr[0], arr[0]
    for n in arr[1:]:
      max1 = max(max1 + n, max0, n)
      max0 = max(max0 + n, n)
      result = max(result, max1)
    return result
