class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        memo = {}

        def dfs(start, visited):
            if start < 0 or start >= n:
                return 0
            if start in memo:
                return memo[start]
            visited[start] = 1
            ret = 1
            for i in range(start - 1, max(0, start - d) - 1, -1):
                if arr[i] >= arr[start]:
                    break
                if visited[i]:
                    continue
                ret = max(ret, dfs(i, visited) + 1)
            for j in range(start + 1, min(start + d, n - 1) + 1):
                if arr[j] >= arr[start]:
                    break
                if visited[j]:
                    continue
                ret = max(ret, dfs(j, visited) + 1)
            visited[start] = 0
            memo[start] = ret
            return ret
        ret = 1
        for i in range(n):
            visited = [0] * n
            ret = max(dfs(i, visited), ret)
        return ret
