class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        prefix = {0: -1}
        res, best, dp = sys.maxsize, sys.maxsize, [sys.maxsize]*len(arr)
        for i, acc in enumerate(itertools.accumulate(arr)):
            if acc-target in prefix:
                end = prefix[acc-target]
                if end > -1:
                    res = min(res, i-end+dp[end])
                best = min(best, i-end)
            dp[i] = best
            prefix[acc] = i
        return -1 if res==sys.maxsize else res

