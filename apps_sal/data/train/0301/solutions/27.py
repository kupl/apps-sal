class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        self.A, self.B = A, B
        self.seen = {}
        return self.dfs(0, 0)

    def dfs(self, a, b):
        m, n = len(self.A), len(self.B)
        if a >= m or b >= n:
            return 0
        if (a, b) in self.seen:
            return self.seen[(a, b)]

        res = float('-inf')
        cur_b = b
        if self.A[a] == self.B[b]:
            res = max(res, self.dfs(a + 1, b + 1) + 1)

        res = max(res, self.dfs(a + 1, b))
        res = max(res, self.dfs(a, b + 1))

        self.seen[(a, b)] = res
        return res
