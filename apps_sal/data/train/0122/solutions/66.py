class Solution:

    def maxScore(self, p: List[int], k: int) -> int:
        res = sum(p[:k])
        cur = res
        for i in range(1, k + 1):
            cur += p[-i] - p[k - i]
            res = max(cur, res)
        return res
