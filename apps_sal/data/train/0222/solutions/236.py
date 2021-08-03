class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        s = set(A)
        l = len(A)
        maxL = 0
        for i in range(l):
            for j in range(i + 1, l):
                a, b = A[i], A[j]
                n = 2
                while a + b in s:
                    a, b = b, a + b
                    n += 1
                if n > 2 and n > maxL:
                    maxL = n
        return maxL
