class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        unique = set(A)
        max_len = 0
        for i in range(len(A) - 2):
            for j in range(i + 1, len(A) - 1):
                (f, s) = (A[i], A[j])
                length = 2
                while f + s in unique:
                    (f, s) = (s, f + s)
                    length += 1
                max_len = max(max_len, length)
        return 0 if max_len == 2 else max_len
