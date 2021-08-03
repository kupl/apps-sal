class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        ans = -math.inf
        left = [-1] * n
        right = [-1] * n
        for i in range(n):
            left[i] = max(arr[i], left[i - 1] + arr[i]) if i > 0 else arr[i]
            ans = max(ans, left[i])
        for i in range(n - 1, -1, -1):
            right[i] = max(arr[i], right[i + 1] + arr[i]) if i < n - 1 else arr[i]
            ans = max(ans, right[i])
        for i in range(1, n - 1):
            ans = max(ans, left[i - 1] + right[i + 1])
        return ans
