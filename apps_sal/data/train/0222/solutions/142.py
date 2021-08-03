class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        dp = []

        for i, x in enumerate(A):
            nd = collections.defaultdict(lambda: 1)
            dp.append(nd)
            for j in range(i):
                prev = x - A[j]
                dp[i][A[j]] = dp[j][prev] + 1
        temp = [max(y.values()) for y in dp if y != {}]
        if temp:
            result = max(temp)
            return result if result >= 3 else 0
        return 0
