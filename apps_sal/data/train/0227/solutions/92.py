class Solution:

    def longestOnes(self, A: List[int], K: int) -> int:
        max_length = 0
        start = 0
        end = 1
        ones = 1
        if len(A) == 0:
            return 0
        if len(A) == 1:
            return 1
        ones = sum(A[:2])
        while end < len(A):
            valid = end - start + 1 - ones <= K
            if valid:
                max_length = max(max_length, end - start + 1)
                end += 1
                if end == len(A):
                    return max_length
                ones += A[end]
            else:
                ones -= A[start]
                start += 1
        return max_length
