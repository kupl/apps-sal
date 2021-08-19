class Solution:

    def helper(self, d, f, target, num_ways):
        if d == 0:
            if target == 0:
                return 1
            else:
                return 0
        if (d, target) in num_ways:
            return num_ways[d, target]
        for face in range(1, f + 1):
            num_ways[d, target] += self.helper(d - 1, f, target - face, num_ways)
        return num_ways[d, target]

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        num_ways = collections.defaultdict(int)
        self.helper(d, f, target, num_ways)
        return num_ways[d, target] % (1000000000 + 7)
