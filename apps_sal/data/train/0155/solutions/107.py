class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [1] * n
        for (a, i) in sorted(([a, i] for (i, a) in enumerate(arr))):
            for di in [-1, 1]:
                for j in range(i + di, i + d * di + di, di):
                    if 0 <= j < n and arr[j] < arr[i]:
                        dp[i] = max(dp[i], dp[j] + 1)
                    else:
                        break
        return max(dp)
