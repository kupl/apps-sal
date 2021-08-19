class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        aSet = set(A)
        dp = collections.defaultdict(int)
        ans = 0
        for i in range(len(A)):
            for j in range(i):
                if A[i] - A[j] < A[j] and A[i] - A[j] in aSet:
                    dp[A[j], A[i]] = dp.get((A[i] - A[j], A[j]), 2) + 1
        return max(dp.values() or [0])
