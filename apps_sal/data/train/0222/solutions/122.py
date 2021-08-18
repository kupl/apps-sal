class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        if len(A) <= 2:
            return 0
        dp = {(A[1], A[0]): 2}
        maxx = 0
        for i in range(2, len(A)):
            j = i - 1
            while j >= 0:
                v = A[i] - A[j]
                if v < A[j] and (A[j], v) in dp:
                    maxx = max(maxx, dp[(A[j], v)] + 1)
                    dp[(A[i], A[j])] = dp[(A[j], v)] + 1
                else:
                    dp[(A[i], A[j])] = 2
                j -= 1
        return maxx
