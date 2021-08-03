class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        dp = {}
        dp[(A[0], A[1])] = 2
        curmax = 2

        for i in range(2, len(A)):
            for j in range(i):
                prev = dp[(A[i] - A[j], A[j])] if (A[i] - A[j], A[j]) in dp else 1
                dp[(A[j], A[i])] = 1 + prev
                curmax = max(curmax, 1 + prev)
        if curmax < 3:
            return 0
        return curmax
