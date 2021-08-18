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
                best = (min(best, i - psum[csum - target]))
                re = min(re, dp[psum[csum - target]] + i - psum[csum - target])
            dp[i] = best
        if re < 100001:
            return re
        return -1
