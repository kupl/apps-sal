class Solution:
    # dp, time O(n^2), space O(n^2)
    '''dp[a, b] represents the length of fibo sequence ends up with (a, b)
Then we have dp[a, b] = (dp[b - a, a] + 1) or 2
    '''
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        dp = collections.defaultdict(int)
        st = set(A)
        for i in range(n):
            for j in range(i + 1, n):
                if A[j] - A[i] < A[i] and A[j] - A[i] in st:
                    dp[A[i], A[j]] = dp.get((A[j] - A[i], A[i]), 2) + 1
        return max(dp.values() or [0])
