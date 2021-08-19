class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mem = collections.defaultdict(int)
        mem[0] = 1
        for i in range(d):
            curr = collections.defaultdict(int)
            for face in range(1, f + 1):
                for (val, count) in list(mem.items()):
                    newVal = face + val
                    if newVal <= target:
                        curr[newVal] += count
            mem = curr
        return mem[target] % (10 ** 9 + 7)
