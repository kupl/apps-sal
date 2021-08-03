class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:

        self.memo = {}

        def helper(start, end, K, prefix):
            if (start, end, K) in self.memo.keys():
                return self.memo[(start, end, K)]

            if K == 0:
                return (prefix[end + 1] - prefix[start]) / (end - start + 1)

            if end == start:
                return prefix[end + 1] - prefix[end]
            if end < start:
                return 0

            maxAvg = 0
            for i in range(start, end):
                maxAvg = max(maxAvg, (prefix[i + 1] - prefix[start]) / (i - start + 1) + helper(i + 1, end, K - 1, prefix))
            self.memo[(start, end, K)] = maxAvg
            return maxAvg

        n = len(A)
        prefix = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + A[i - 1]

        ans = 0
        for k in range(K):
            ans = max(ans, helper(0, n - 1, k, prefix))

        return ans
