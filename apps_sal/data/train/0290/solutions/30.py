import sys


class Solution:

    def __init__(self):
        self.dp = {}

    def minCost(self, A: int, B: List[int]) -> int:
        self.set1 = set(B)

        def helper(st, end):
            if (st, end) in self.dp:
                return self.dp[st, end]
            if end - st == 1:
                return 0
            t = sys.maxsize
            for i in B:
                if i > st and i < end:
                    t = min(t, end - st + helper(st, i) + helper(i, end))
            self.dp[st, end] = t if t != sys.maxsize else 0
            return self.dp[st, end]
        helper(0, A)
        return self.dp[0, A]
