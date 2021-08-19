# REMEMBER: WHERE TO PUT THE MEMOIZE SAVE AND LOOKUP LINES IN THE RECURSIVE FUNCTION.
# 1. BEFORE any work is done + AFTER all the work is done and we're about to return the answer.

class Solution:
    def __init__(self):
        self.memo = {}  # maps (d, target) to num ways.

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # obvious base case.
        if d * f < target:
            return 0
        if d == 1:
            return 1

        if (d, target) in self.memo:
            return self.memo[(d, target)]
        # we do it recursively
        numWays = 0
        for i in range(f, 0, -1):
            # for i in range(1, f+1):
            # we roll with i, then we
            if target - i > 0:
                ways = self.memo.get((d - 1, target - i), self.numRollsToTarget(d - 1, f, target - i))
                numWays += ways
        self.memo[(d, target)] = numWays
        return numWays % (10**9 + 7)
