class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:

        def helper(arr, index, d, memo):
            if arr[index] < 0 or not 0 <= index < len(arr):
                return 0
            if index in memo:
                return memo[index]
            left_visited = 0
            right_visited = 0
            arr[index] = -arr[index]
            for i in range(index + 1, index + d + 1):
                if i >= len(arr):
                    break
                if abs(arr[i]) >= abs(arr[index]):
                    break
                if arr[i] < 0:
                    continue
                left_visited = max(left_visited, helper(arr, i, d, memo))
            for j in range(index - 1, index - d - 1, -1):
                if j < 0:
                    break
                if abs(arr[j]) >= abs(arr[index]):
                    break
                if arr[j] < 0:
                    continue
                right_visited = max(right_visited, helper(arr, j, d, memo))
            arr[index] = -arr[index]
            memo[index] = 1 + max(left_visited, right_visited)
            return memo[index]
        max_visited = 1
        p = False
        memo = {}
        for index in range(len(arr)):
            visited = helper(arr, index, d, memo)
            max_visited = max(visited, max_visited)
        return max_visited
