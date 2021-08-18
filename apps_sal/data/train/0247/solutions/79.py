class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        psum = {0: -1}
        csum = 0
        re = 100001
        dp = [100001] * (len(arr))
        best = 100001
        for i, csum in enumerate(itertools.accumulate(arr)):
            psum[csum] = i
            if csum - target in psum:
                end = psum[csum - target]
                best = (min(best, i - end))
                if end > -1:
                    re = min(re, dp[end] + i - end)
            dp[i] = best
        if re < 100001:
            return re
        return -1
