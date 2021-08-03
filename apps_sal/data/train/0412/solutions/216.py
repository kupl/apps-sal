class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        m = collections.defaultdict(int)
        m[(0, 0)] = 0
        for t in range(1, 1 + f):
            m[(1, t)] = 1
        for i in range(1, 1 + d):
            for j in range(1, 1 + target):
                for k in range(1, min(1 + f, j)):
                    m[(i, j)] += m[(i - 1, j - k)]
        return m[(d, target)] % (10**9 + 7)
