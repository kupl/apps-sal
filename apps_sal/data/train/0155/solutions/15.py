class Solution:
    from collections import deque

    def maxJumps(self, arr: List[int], d: int) -> int:
        q = deque()
        n = len(arr)
        dp = [-1] * n

        def solve(node):
            if node < 0 or node >= n:
                return -1

            if dp[node] != -1:
                return dp[node]

            ans = 0
            for i in range(1, d + 1):
                if node + i >= n or arr[node + i] >= arr[node]:
                    break
                ans = max(ans, solve(i + node))

            for i in range(1, d + 1):
                if node - i < 0 or arr[node - i] >= arr[node]:
                    break
                ans = max(ans, solve(node - i))

            dp[node] = 1 + ans

            return dp[node]

        for i in range(n):
            solve(i)

        return max(dp)
