class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        dp = {}

        for i in range(1, len(A)):
            for j in range(i):
                dp[(A[j], A[i])] = max(dp.get((A[j], A[i]), 2), dp.get((A[i] - A[j], A[j]), 1) + 1)

        res = max(dp.values())
        return res if res > 2 else 0
