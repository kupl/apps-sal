class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:
        m = len(arr)
        memo = [-1 for _ in range(m)]

        def dfs(i):
            if memo[i] != -1:
                return memo[i]
            memo[i] = 1
            left = i - 1
            while left >= 0 and i - left <= d and (arr[left] < arr[i]):
                memo[i] = max(dfs(left) + 1, memo[i])
                left -= 1
            right = i + 1
            while right < m and right - i <= d and (arr[right] < arr[i]):
                memo[i] = max(dfs(right) + 1, memo[i])
                right += 1
            return memo[i]
        for i in range(m):
            dfs(i)
        print(memo)
        return max(memo)
