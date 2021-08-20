class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        if arrLen == 0 or (arrLen == 1 and steps > 0):
            return arrLen
        combos = {}

        def _dfs_ways(steps, arrLen, loc=0, tar=0):
            if steps == 0:
                return 1 if loc == tar else 0
            if (steps, loc) in combos:
                return combos[steps, loc]
            steps -= 1
            stay = _dfs_ways(steps, arrLen, loc)
            left = _dfs_ways(steps, arrLen, loc - 1) if loc - 1 >= 0 else 0
            right = _dfs_ways(steps, arrLen, loc + 1) if loc + 1 < arrLen else 0
            res = int((left + right + stay) % (math.pow(10, 9) + 7))
            steps += 1
            combos[steps, loc] = res
            return res
        _dfs_ways(steps, arrLen)
        ans = combos[steps, 0]
        return int(ans % (math.pow(10, 9) + 7))
