import functools
@functools.lru_cache(maxsize=10**7+1)
def count(curr, maxpos, steps, mod):
    if curr < 0: return 0
    if curr == maxpos: return 0
    if steps == 1 and curr == 1: return 1
    if steps == 1 and curr == 0: return 1
    if steps == 0: return 0
    return (count(curr, maxpos, steps-1, mod)%mod + count(curr+1, maxpos, steps-1, mod)%mod + count(curr-1, maxpos, steps-1, mod)%mod)%mod

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        curr = 0
        mod = 10**9+7
        return count(curr, arrLen, steps, mod)
