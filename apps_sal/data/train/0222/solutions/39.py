class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        set_a = set(A)
        res = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                x, y = A[i], A[j]
                leng = 2
                while x + y in set_a:
                    x, y = y, x + y
                    leng += 1
                res = max(res, leng)
        return res if res >= 3 else 0
