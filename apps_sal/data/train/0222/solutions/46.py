class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        s = set(A)
        res = 2
        for i in range(n):
            for j in range(i + 1, n):
                (a, b, l) = (A[i], A[j], 2)
                while a + b in s:
                    (a, b, l) = (b, a + b, l + 1)
                res = max(res, l)
        return res if res > 2 else 0
