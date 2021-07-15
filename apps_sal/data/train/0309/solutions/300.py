class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        memo = collections.defaultdict(dict)
        ans = 0
        
        for i, a2 in enumerate(A):
            for j in range(i):
                a1 = A[j]
                diff = a2 - a1
                memo[i][diff] = 2
                if diff in memo[j]:
                    memo[i][diff] = max(memo[i][diff], memo[j][diff] + 1)
                ans = max(ans, memo[i][diff])
        return ans
