class Solution:

    def maxScore(self, p: List[int], k: int) -> int:
        s = sum(p)
        if k == len(p):
            return s
        n = len(p)
        for i in range(1, len(p)):
            p[i] += p[i - 1]
        return s - min((p[n + i - k - 1] - (p[i - 1] if i else 0) for i in range(k + 1)))
