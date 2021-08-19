class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        (n, s, res) = (len(A), set(A), 0)
        for i in range(n):
            for j in range(i + 1, n):
                (x, y, l) = (A[j], A[i] + A[j], 2)
                while y in s:
                    (x, y) = (y, x + y)
                    l += 1
                res = max(res, l)
        return res if res > 2 else 0
