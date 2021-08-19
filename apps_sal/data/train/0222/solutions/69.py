class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        if len(A) == 0:
            return A
        result = 0
        aref = set(A)
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                (x, y) = (A[j], A[i] + A[j])
                seq_length = 0
                while y in aref:
                    if seq_length == 0:
                        seq_length = 2
                    seq_length += 1
                    (x, y) = (y, x + y)
                result = max(result, seq_length)
        return result
