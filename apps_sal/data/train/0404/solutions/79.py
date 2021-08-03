class Solution(object):
    def largestSumOfAverages(self, A, K):
        memo = {}

        def search(n, k):
            if (n, k) in memo:
                return memo[n, k]
            if n < k:
                return 0
            if k == 1:
                memo[n, k] = sum(A[:n]) / float(n)
                return memo[n, k]
            cur = 0
            res = 0
            for i in range(n - 1, 0, -1):
                cur += A[i]
                res = max(res, search(i, k - 1) + cur / float(n - i))
            memo[n, k] = res
            return memo[n, k]
        return search(len(A), K)
