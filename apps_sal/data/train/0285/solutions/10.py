class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        minn, maxx = A[0], A[-1]
        ans = maxx - minn
        for i in range(len(A) - 1):
            a, b = A[i], A[i + 1]
            ans = min(ans, max(maxx - K, a + K) - min(minn + K, b - K))
        return ans
