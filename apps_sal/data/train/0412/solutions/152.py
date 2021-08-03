class Solution:

    def __init__(self):
        self.cache = dict()

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:

        def helper(d, r):

            if d < 0 or r < 0:
                return 0

            if d == 0 and r == 0:
                return 1

            elif d != 0 and r != 0:

                if (d, r) not in self.cache:

                    self.cache[(d, r)] = 0

                    for i in range(1, f + 1):
                        self.cache[(d, r)] += helper(d - 1, r - i)

                return self.cache[(d, r)]

            else:
                return 0

        return helper(d, target) % (10**9 + 7)
