class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        self.dp = collections.defaultdict(int)
        return self.helper(0, steps, arrLen)

    def helper(self, cur, steps, n):
        x = (pow(10, 9) + 7)
        if(cur == 0 and steps == 0):
            return 1
        if(abs(cur) > steps or cur < 0 or cur >= n):
            return 0
        if((cur, steps) in self.dp):
            return self.dp[(cur, steps)]

        res = self.helper(cur, steps - 1, n) + self.helper(cur - 1, steps - 1, n) + self.helper(cur + 1, steps - 1, n)
        self.dp[(cur, steps)] = res % x
        return res % x
