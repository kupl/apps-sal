class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        s = set(A)
        dp = defaultdict(int)
        ans = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                (prev, curr, l) = (A[i], A[j], 0)
                while prev + curr in s:
                    l += 1
                    dp[prev + curr] = l
                    (prev, curr) = (curr, prev + curr)
                ans = max(ans, l)
        return ans + 2 if ans > 0 else 0
