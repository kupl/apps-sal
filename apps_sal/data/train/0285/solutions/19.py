

class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:

        A.sort()

        min_diff = A[-1] - A[0]

        for i in range(len(A) - 1):
            v_min = min(A[0] + K, A[i + 1] - K)
            v_max = max(A[i] + K, A[-1] - K)

            min_diff = min(min_diff, v_max - v_min)

        return min_diff
