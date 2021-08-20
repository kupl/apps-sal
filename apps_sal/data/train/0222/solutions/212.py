class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        s = set(A)
        res = 0
        for i in range(len(A) - 2):
            for j in range(i + 1, len(A) - 1):
                (a, b) = (A[i], A[j])
                cnt = 2
                while a + b in s:
                    (a, b) = (b, a + b)
                    cnt += 1
                    res = max(res, cnt)
        return res
