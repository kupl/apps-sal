
def count(curr, maxpos, steps, mod, obj):
    if curr < 0:
        return 0
    if curr == maxpos:
        return 0
    if steps == 1 and curr == 1:
        return 1
    if steps == 1 and curr == 0:
        return 1
    if steps == 0:
        return 0
    if (curr, steps) in obj:
        return obj[(curr, steps)]
    obj[(curr, steps)] = (count(curr, maxpos, steps - 1, mod, obj) % mod + count(curr + 1, maxpos, steps - 1, mod, obj) % mod + count(curr - 1, maxpos, steps - 1, mod, obj) % mod) % mod
    return obj[(curr, steps)]


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        curr = 0
        mod = 10**9 + 7
        obj = {}
        return count(curr, arrLen, steps, mod, obj)
