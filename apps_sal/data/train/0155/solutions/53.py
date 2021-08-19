class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:

        @lru_cache(None)
        def dfs(i):
            if i == 0 and i + 1 < len(arr):
                if arr[i] <= arr[i + 1]:
                    return 1
            elif i == len(arr) - 1 and i - 1 >= 0:
                if arr[i] <= arr[i - 1]:
                    return 1
            elif i - 1 >= 0 and i + 1 < len(arr) and (arr[i] <= arr[i - 1]) and (arr[i] <= arr[i + 1]):
                return 1
            left_step = 1
            for j in range(i + 1, i + d + 1):
                if j >= len(arr) or arr[j] >= arr[i]:
                    break
                left_step = max(left_step, 1 + dfs(j))
            right_step = 1
            for j in range(i - 1, i - d - 1, -1):
                if j < 0 or arr[j] >= arr[i]:
                    break
                right_step = max(right_step, 1 + dfs(j))
            return max(left_step, right_step)
        max_step = 0
        for i in range(len(arr)):
            max_step = max(max_step, dfs(i))
        return max_step
