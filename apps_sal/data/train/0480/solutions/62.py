class Solution:
    # 了解和对比TC
    # dfs to find all possible way - dfs + dp: cutting rope
    # state: remaining steps + distance
    # - break to two parts which sum of remain steps == total steps
    # - sum of dist <= arrLen
    # - takes 1 extra steps to connect
    def numWays(self, steps: int, arrLen: int) -> int:
        # if dist == 1, combos always 1 regardless of steps
        if arrLen == 0 or (arrLen == 1 and steps > 0):
            return arrLen
        combos = {}  # (dist, steps): # of combos

        def _dfs_ways(steps, arrLen, loc=0, tar=0):
            if steps == 0:
                return 1 if loc == tar else 0
            if (steps, loc) in combos:
                return combos[(steps, loc)]
            steps -= 1
            stay, right, left = 0, 0, 0
            stay = _dfs_ways(steps, arrLen, loc)
            if loc + 1 < arrLen:
                right = _dfs_ways(steps, arrLen, loc + 1)
            if loc - 1 >= 0:
                left = _dfs_ways(steps, arrLen, loc - 1)
            steps += 1
            res = (stay + left + right) % (math.pow(10, 9) + 7)
            combos[(steps, loc)] = res
            return res

        # for i in range(1, min(arrLen, steps // 2) + 1):
        #     # for combo two parts
        #     res = 0
        #     for div in range(1, i + 1): # divide len for dfs
        #         for left_steps in range(1, steps):
        #             left_ways = _dfs(left_steps, div)
        #             right_ways = _dfs(steps - left_steps - 1, i - div)
        #             res += left_ways * right_ways
        #     # for whole
        #     res += _dfs(steps, i)
        #     combos[(steps, i)] = res
        _dfs_ways(steps, arrLen)
        # print(combos)
        ans = combos[(steps, 0)]
        return int(ans % (math.pow(10, 9) + 7))
