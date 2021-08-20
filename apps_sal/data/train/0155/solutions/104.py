class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:
        memo = [-1] * len(arr)

        def dfs(i):
            if i < 0 or i >= len(arr):
                return 0
            if memo[i] > 0:
                return memo[i]
            memo[i] = 1
            for j in reversed(list(range(max(0, i - d), i))):
                if arr[j] >= arr[i]:
                    break
                memo[i] = max(memo[i], dfs(j) + 1)
            for j in range(i + 1, min(len(arr), i + d + 1)):
                if arr[j] >= arr[i]:
                    break
                memo[i] = max(memo[i], dfs(j) + 1)
            return memo[i]
        return max((dfs(i) for i in range(len(arr))))
