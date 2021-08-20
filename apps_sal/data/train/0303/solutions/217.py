class Solution:

    @lru_cache(None)
    def rec(self, idx):
        if idx > len(self.A):
            return 0
        max_yet = 0
        max_score = 0
        for i in range(self.K):
            if idx + i >= len(self.A):
                break
            max_yet = max(max_yet, self.A[idx + i])
            max_score = max(max_score, max_yet * (i + 1) + self.rec(idx + i + 1))
        return max_score

    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        self.A = A
        self.K = K
        return self.rec(0)
