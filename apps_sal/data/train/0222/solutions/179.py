class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        dp = collections.defaultdict(lambda: 2)
        ret, idx = 0, {A[0]:0}
        for j in range(1, len(A) -1):
            idx[A[j]] = j
            
            for i in range(j+1, len(A)):
                diff = A[i] - A[j]

                if diff >= A[j]:
                    break
                elif diff not in idx:
                    continue
                dp[j,i] = dp[idx[diff], j] +1
                ret = max(ret, dp[j,i])
        return ret

