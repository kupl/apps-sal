class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        self.dp = {}

        def recur_top_down(d, f, target):
            if d == 0:
                return 1 if target == 0 else 0
            if (d, target) in self.dp:
                return self.dp[d, target]
            res = 0
            for i in range(f):
                res += recur_top_down(d - 1, f, target - (i + 1)) % (10 ** 9 + 7)
            res = res % (10 ** 9 + 7)
            self.dp[d, target] = res
            return res
        return recur_top_down(d, f, target)
