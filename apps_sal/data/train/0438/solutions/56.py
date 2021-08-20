class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        dp = [0] * (len(arr) + 2)
        g = collections.Counter()
        ans = -1
        for i in range(len(arr)):
            (l, r) = (dp[arr[i] - 1], dp[arr[i] + 1])
            dp[arr[i]] = l + r + 1
            dp[arr[i] - l] = dp[arr[i] + r] = l + r + 1
            g[l] -= 1
            g[r] -= 1
            g[dp[arr[i]]] += 1
            if g[m] > 0:
                ans = i + 1
        return ans
