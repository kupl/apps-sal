class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        prefix = [0] + A.copy()
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i - 1]

        def query(i, j):  # inclusive
            return prefix[j + 1] - prefix[i]

        def get_average(i, j):
            return query(i, j) / (j - i + 1)

        N = len(A)
        cache = {}

        def dfs(i, k):
            if k < 0:
                return -float('inf')

            if (i, k) in cache:
                return cache[(i, k)]

            if i == N:
                if k == 0:
                    return 0
                else:
                    return -float('inf')

            res = -float('inf')
            for j in range(i, N):
                take = dfs(j + 1, k - 1) + get_average(i, j)
                res = max(res, take)

            cache[(i, k)] = res
            return res

        return dfs(0, K)
