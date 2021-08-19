class Solution:

    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        n = len(A)
        memo = [[0 for k in range(K)] for i in range(n)]

        def aux(A, cur, k, memo):
            if cur == len(A):
                return 0
            if memo[cur][k]:
                return memo[cur][k]
            tmp = sum(A[cur:]) / (len(A) - cur)
            if k == 0:
                memo[cur][k] = tmp
                return tmp
            for i in range(cur + 1, len(A) + 1):
                tmp = max(tmp, sum(A[cur:i]) / (i - cur) + aux(A, i, k - 1, memo))
            memo[cur][k] = tmp
            return tmp
        return aux(A, 0, K - 1, memo)
