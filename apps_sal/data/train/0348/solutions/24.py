class Solution:

    def maximumSum(self, arr: List[int]) -> int:
        (mx, n) = (float('-inf'), len(arr))
        (left, right) = ([float('-inf') for _ in range(len(arr))], [float('-inf') for _ in range(len(arr))])
        for i in range(len(arr)):
            left[i] = max(arr[i], arr[i] + left[i - 1]) if i > 0 else arr[0]
            right[n - i - 1] = max(arr[n - i - 1], arr[n - i - 1] + right[n - i]) if i > 0 else arr[-1]
        for i in range(len(arr)):
            mx = max(mx, arr[i])
            if 2 * arr[i] != left[i] + right[i]:
                mx = max(mx, left[i] + right[i] - 2 * arr[i])
        return mx
