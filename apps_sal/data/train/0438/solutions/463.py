class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        size = {i: 1 for i in range(n)}
        dp = [*range(n)]
        res = -1

        def union(i, j):
            size_count[size[find(i)]] -= 1
            size_count[size[find(j)]] -= 1
            tmp = size[find(i)] + size[find(j)]
            size_count[tmp] += 1
            size[find(i)] = size[find(j)] = tmp
            dp[find(i)] = dp[find(j)]

        def find(i):
            if i != dp[i]:
                dp[i] = find(dp[i])
            return dp[i]
        curr = [0] * n
        size_count = [0] * (n + 1)
        for (k, i) in enumerate([x - 1 for x in arr]):
            curr[i] = 1
            size_count[1] += 1
            if i < n - 1 and curr[i + 1]:
                union(i, i + 1)
            if i and curr[i - 1]:
                union(i, i - 1)
            if size_count[m] > 0:
                res = k + 1
        return res
