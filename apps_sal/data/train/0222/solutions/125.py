class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        S = set(A)
        res = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                (f1, f2) = (A[i], A[j])
                length = 0
                if f1 + f2 in S:
                    length = 2
                while f1 + f2 in S:
                    length += 1
                    tmp = f1 + f2
                    f1 = f2
                    f2 = tmp
                res = max(length, res)
        return res
