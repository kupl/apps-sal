class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:
        res = 0
        visited = {}

        def dfs(i):
            if i in visited:
                return visited[i]
            step = 1
            i_right = i + 1
            while i_right < len(arr) and i_right - i <= d:
                if arr[i_right] >= arr[i]:
                    break
                step = max(step, 1 + dfs(i_right))
                i_right += 1
            i_left = i - 1
            while i_left >= 0 and i - i_left <= d:
                if arr[i_left] >= arr[i]:
                    break
                step = max(step, 1 + dfs(i_left))
                i_left -= 1
            visited[i] = step
            return step
        for i in range(len(arr)):
            res = max(res, dfs(i))
        return res
