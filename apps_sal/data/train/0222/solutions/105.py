class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        dp = [[2]*n for i in range(n)]

        map_ = collections.defaultdict(int)
        for i,j in enumerate(A):
            map_[j] = i

        # i:end  j:start

        for i in range(2, n):
            for j in range(1, i):
                diff = A[i] - A[j]
                
                if diff in list(map_.keys()) and map_[diff] < j:
                    k = map_[diff]
                    dp[j][i] = max(dp[j][i], dp[k][j] + 1)

        max_ = max(dp[j][i] for i in range(n) for j in range(n))

        if max_ == 2:
            return 0
        else:
            return max_


