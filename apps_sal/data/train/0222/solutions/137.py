class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        s = set(A)
        longest = 2
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                (x, y) = (A[i], A[j])
                seqlen = 2
                while x + y in s:
                    (x, y) = (y, x + y)
                    seqlen += 1
                longest = max(seqlen, longest)
        return longest if longest > 2 else 0
