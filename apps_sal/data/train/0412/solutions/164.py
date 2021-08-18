class Solution:
    def helper(self, d, f, target, dp):
        if d == 0:
            return 1 if target == 0 else 0
        if (target, d) in dp:
            return dp[(target, d)]
        for i in range(1, f + 1):
            dp[(target, d)] += self.helper(d - 1, f, target - i, dp)
        return dp[(target, d)]

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = Counter()
        return self.helper(d, f, target, dp) % (pow(10, 9) + 7)
