class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:

        @lru_cache(None)
        def max_connections(A_index, B_index):
            if A_index > len(A) - 1 or B_index > len(B) - 1:
                return 0
            if A[A_index] == B[B_index]:
                return max(0, 1 + max_connections(A_index + 1, B_index + 1))
            else:
                return max(0, max_connections(A_index + 1, B_index), max_connections(A_index, B_index + 1))
        return max_connections(0, 0)
