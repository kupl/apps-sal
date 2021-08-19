class Solution:

    def lenLongestFibSubseq(self, A: 'List[int]') -> 'int':
        map = collections.defaultdict(int)
        for (i, v) in enumerate(A):
            map[v] = i
        n = len(A)
        dp = [[2 for _ in range(n + 1)] for _ in range(n + 1)]
        for j in range(n):
            for i in range(j):
                diff = A[j] - A[i]
                if diff in map and diff < A[i]:
                    k = map[diff]
                    dp[i][j] = max(dp[i][j], 1 + dp[k][i])
        ans = max([max(n) for n in dp])
        return 0 if ans <= 2 else ans
