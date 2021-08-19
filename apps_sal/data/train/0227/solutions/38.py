"""

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6







"""


class Solution:

    def longestOnes(self, A: List[int], K: int) -> int:
        """
        Sliding window technique
        """
        if not A:
            return 0
        window = 0
        start = 0
        max_ones = 0
        for (it, value) in enumerate(A):
            window += value
            if it - start + 1 > window + K:
                window -= A[start]
                start += 1
            max_ones = max(max_ones, window + K)
        return min(max_ones, len(A))
