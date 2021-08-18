class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)

        h = {0: -1}
        preSum = [0 for i in range(n)]
        for i in range(n):
            preSum[i] = preSum[i - 1] + arr[i] if i > 0 else arr[0]
            h[preSum[i]] = i
        left = [n + 1 for i in range(n)]
        ans = n + 1
        for i in range(n):
            if preSum[i] - target in h:
                left[i] = i - h[preSum[i] - target]
            if i > 0:
                left[i] = min(left[i - 1], left[i])
            if left[i] < n + 1 and preSum[i] + target in h:
                right = h[preSum[i] + target] - i
                ans = min(ans, left[i] + right)
        return ans if ans < n + 1 else -1
