class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        res = 2
        s = set(A)
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                (a, b, l) = (A[i], A[j], 2)
                while a + b in s:
                    (a, b) = (b, a + b)
                    l += 1
                res = max(res, l)
        print(res)
        if res > 2:
            return res
        else:
            return 0
