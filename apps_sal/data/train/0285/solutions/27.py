class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:

        A.sort()

        min_diff = A[-1] - A[0]

        for i in range(len(A) - 1):
            # vs=[A[0]+K,A[i]+K,A[i+1]-K,A[-1]-K]

            v_min = min(A[0] + K, A[i + 1] - K)
            v_max = max(A[i] + K, A[-1] - K)

            min_diff = min(min_diff, max(v_min, v_max) - min(v_min, v_max))

        return min_diff
