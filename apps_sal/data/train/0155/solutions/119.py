class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        dp = [-1 for _ in range(len(arr))]

        def dp_memo(x):
            if dp[x] != -1:
                return dp[x]

            dp[x] = 1
            for y in range(x-1, x-d-1, -1):
                if y < 0 or arr[y] >= arr[x]:
                    break
                dp[x] = max(dp[x], 1 + dp_memo(y))

            for y in range(x+1, x+d+1, +1):
                if y >= len(arr) or arr[y] >= arr[x]:
                    break
                dp[x] = max(dp[x], 1 + dp_memo(y))
            return dp[x]

        for i in range(len(arr)):
            dp_memo(i)
        print(dp)
        return max(dp)
