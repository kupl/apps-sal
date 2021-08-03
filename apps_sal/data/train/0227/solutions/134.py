class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        le, ri = 0, 0
        max_len = 0
        while ri < len(A):
            if A[ri] == 0:
                K -= 1
            ri += 1
            if K >= 0:
                max_len = max(max_len, ri - le)
            print((le, ri))
            while K < 0 and le < ri:
                if A[le] == 0:
                    K += 1
                le += 1

        return max_len
