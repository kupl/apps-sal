class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)

        h = {0: -1}
        preSum = 0
        for i in range(n):
            preSum = preSum + arr[i] if i > 0 else arr[0]
            h[preSum] = i
        ans = n + 1
        left = n + 1
        preSum = 0
        for i in range(n):
            preSum += arr[i]
            if preSum - target in h:
                left = min(left, i - h[preSum - target])
            if left < n + 1 and preSum + target in h:
                right = h[preSum + target] - i
                ans = min(ans, left + right)
        return ans if ans < n + 1 else -1
