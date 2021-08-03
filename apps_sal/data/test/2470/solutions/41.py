import bisect


class Solution:
    def recurse(self, arr1, arr2, m, n, idx, prev, dp):
        if idx >= n:
            return 0
        k = bisect.bisect_right(arr2, prev)
        if dp[idx][k] != -1:
            return dp[idx][k]
        c1 = self.recurse(arr1, arr2, m, n, idx + 1, arr1[idx], dp) if arr1[idx] > prev else 2000
        c2 = 1 + self.recurse(arr1, arr2, m, n, idx + 1, arr2[k], dp) if k < m else 2000
        dp[idx][k] = min(c1, c2)
        return dp[idx][k]

    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        dp = [[-1 for i in range(2001)] for j in range(2001)]
        arr2.sort()
        ans = self.recurse(arr1, arr2, len(arr2), len(arr1), 0, -10**9, dp)
        if ans >= 2000:
            return -1
        else:
            return ans
