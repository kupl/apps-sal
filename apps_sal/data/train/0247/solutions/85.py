class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        dp = [100001] * (n)
        presum = {0: -1}
        s = 0
        ans = 100001
        best_so_far = sys.maxsize
        for i in range(n):
            s += arr[i]
            presum[s] = i

            if s - target in presum:
                j = presum[s - target]
                best_so_far = min(best_so_far, i - j)
                if j >= 0:
                    ans = min(ans, dp[j] + i - j)

            dp[i] = best_so_far

        return ans if ans < 100001 else -1
