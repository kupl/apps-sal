class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        s = set(A)
        res = 2
        for i in range(len(A) - 2):
            for j in range(i + 1, len(A) - 1):
                (a, b) = (A[i], A[j])
                cnt = 2
                while a + b in s:
                    cnt += 1
                    res = max(res, cnt)
                    (a, b) = (b, a + b)
        return res if res > 2 else 0
