class Solution:

    def longestOnes(self, A: List[int], K: int) -> int:
        (start, end) = (0, 0)
        for end in range(len(A)):
            if A[end] == 0:
                K -= 1
            if K < 0:
                if A[start] == 0:
                    K += 1
                start += 1
        return end - start + 1
