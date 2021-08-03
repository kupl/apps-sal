class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        # only need the first 2 elements to define a fib seq
        setA = set(A)
        rint = 0

        def getLen(i, j):
            a, b = A[i], A[j]
            if a + b not in setA:
                return 0
            length = 2
            while a + b in setA:
                length += 1
                a, b = b, a + b
            return length
        for i in range(len(A) - 2):
            for j in range(i + 1, len(A) - 1):
                if A[j] - A[i] in setA and A[j] - A[i] < A[i]:
                    continue
                rint = max(rint, getLen(i, j))
                # print(i, j, getLen(i, j))
        return rint
