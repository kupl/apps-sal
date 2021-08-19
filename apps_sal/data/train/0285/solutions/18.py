class Solution:

    def smallestRangeII(self, A: List[int], K: int) -> int:
        if K == 0:
            return max(A) - min(A)
        if len(A) == 1:
            return 0
        if max(A) - min(A) <= K:
            return max(A) - min(A)
        else:
            A = sorted(A)
            dp = [A[-1] - A[0]]
            (n1, n2) = (A[-1] - K, A[0] + K)
            for i in range(len(A) - 1):
                dp += [max(A[i] + K, n1) - min(n2, A[i + 1] - K)]
            return min(dp)
