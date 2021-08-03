class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        if not A or len(A) < K:
            return 0
        for i in range(1, len(A)):
            A[i] += A[i - 1]

        cache = {}

        def cal(n, k):
            if n <= 0 or k <= 0:
                return 0
            if n < k:
                return 0
            if (n, k) in cache:
                return cache[(n, k)]
            if k == 1:
                cache[(n, 1)] = A[n - 1] / n
                return cache[(n, 1)]
            res, cur = 0, 0
            for i in range(n - 1, 0, -1):
                res = max(res, (A[n - 1] - A[i - 1]) / (n - i) + cal(i, k - 1))
            cache[(n, k)] = res
            return res

        return cal(len(A), K)
