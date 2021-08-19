class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        mi, ma = A[0], A[-1]
        # Note: using K will only possibly reduce the current difference
        ans = ma - mi  # the modified result will not be greater than the current worsest case (max(A)-min(A))
        for i in range(len(A) - 1):
            a, b = A[i], A[i + 1]
            ans = min(ans, max(ma - K, a + K) - min(mi + K, b - K))
        return ans
