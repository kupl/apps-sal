class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        index = {x:i for i, x in enumerate(A)}
        dp = collections.defaultdict(lambda:2)
        
        ans = 0
        for k, z in enumerate(A):
            for j in range(k):
                i = index.get(z-A[j], None)
                if i is not None and i<j:
                    cand = dp[j, k] = dp[i, j]+1
                    ans = max(ans, cand)
        
        return ans if ans>=3 else 0
