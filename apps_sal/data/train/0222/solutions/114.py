class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        N = len(A)
        st = set(A)
        res = 2
        for i in range(N):
            for j in range(i + 1, N):
                a, b, l = A[i], A[j], 2
                while a + b in st:
                    a, b, l = b, a + b, l + 1
                res = max(res, l)
        return res if res > 2 else 0
