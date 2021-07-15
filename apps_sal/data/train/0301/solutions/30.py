from functools import lru_cache


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        
        len_a = len(A)
        len_b = len(B)
        
        @lru_cache(None)
        def helper(i, j):
            nonlocal A, B, len_a, len_b, b_index_data

            if i >= len_a or j >= len_b:
                return 0

            ans = float('-inf')
            for x in b_index_data.get(A[i], []):
                if x >= j:
                    ans = 1 + helper(i + 1, x + 1)
                    break
            return max(ans, helper(i + 1, j))

        b_index_data = {}
        for i, val in enumerate(B):
            l = b_index_data.setdefault(val, [])
            l.append(i)

        return helper(0, 0)

