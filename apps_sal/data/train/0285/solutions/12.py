

class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        arr_min, arr_max = A[0], A[-1]
        ans = arr_max - arr_min
        for i in range(len(A) - 1):
            a, b = A[i], A[i + 1]
            ans = min(ans, max(arr_max - K, a + K) - min(arr_min + K, b - K))
        return ans
