class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [1 for i in range(n)]
        p = []
        for (idx, x) in enumerate(arr):
            p.append((x, idx))
        p.sort(reverse=True)
        for i in range(n):
            idx = p[i][1]
            for j in range(idx + 1, min(n, d + idx + 1)):
                if arr[j] >= arr[idx]:
                    break
                dp[j] = max(dp[j], dp[idx] + 1)
            for j in range(idx - 1, max(-1, idx - d - 1), -1):
                if arr[j] >= arr[idx]:
                    break
                dp[j] = max(dp[j], dp[idx] + 1)
        return max([dp[i] for i in range(n)])
