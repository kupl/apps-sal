class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        memo = {}

        def dfs(i):
            if arr[i] == 0:
                return True
            if i in memo:
                return memo[i]
            memo[i] = False
            new_i = i + arr[i]
            if 0 <= new_i < len(arr):
                if dfs(new_i):
                    memo[i] = True
                    return True
            new_i = i - arr[i]
            if 0 <= new_i < len(arr):
                if dfs(new_i):
                    memo[i] = True
                    return True

            return memo[i]

        return dfs(start)
