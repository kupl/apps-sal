class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        A.sort()
        S = (set(A))
        maxlen = 0

        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                a, b = A[j], A[i] + A[j]
                count = 2
                while b in S:
                    count += 1
                    a, b = b, a + b
                maxlen = max(maxlen, count)
        if maxlen >= 3:
            return maxlen
        return 0
