class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        inf = sum(jobDifficulty)
        mem = {}
        def dfs(i, d):
            if (i, d) in mem:
                return mem[(i, d)]
            if d == 0:
                if i == len(jobDifficulty):
                    mem[(i, d)] = (True, 0)
                    return True, 0
                else:
                    mem[(i, d)] = (False, None)
                    return False, inf
            else:
                success = False
                min_diff = inf
                cur_day_diff = 0
                for end in range(i, len(jobDifficulty)-d+1):
                    cur_day_diff = max(cur_day_diff, jobDifficulty[end])
                    next_success, next_diff = dfs(end+1, d-1)
                    if next_success:
                        success = True
                        min_diff = min(min_diff, cur_day_diff+next_diff)
                mem[(i, d)] = (success, min_diff)
                return success, min_diff
        success, min_diff = dfs(0, d)
        if success:
            return min_diff
        else:
            return -1

