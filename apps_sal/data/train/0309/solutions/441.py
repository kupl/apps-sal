class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        if n < 3:
            return n
        self.memo = {}
        self.res = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                diff = A[j] - A[i]
                if (i, diff) in self.memo:
                    self.memo[j, diff] = self.memo[i, diff] + 1
                else:
                    self.memo[j, diff] = 2
                self.res = max(self.res, self.memo[j, diff])
        return self.res
