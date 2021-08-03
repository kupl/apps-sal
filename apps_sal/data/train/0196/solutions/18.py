class Solution:
    def maxSubarraySumCircular(self, a: List[int]) -> int:
        n = len(a)
        ans = float('-inf')
        current = 0
        for num in a:
            current = num + max(0, current)
            ans = max(ans, current)

        right_sum = [0] * n
        right_sum[-1] = a[-1]
        right_most = [float('-inf')] * n
        right_most[-1] = right_sum[-1]
        for i in range(n - 2, -1, -1):
            right_sum[i] = right_sum[i + 1] + a[i]
            right_most[i] = max(right_sum[i], right_most[i + 1])
        left_sum = 0
        for i in range(n - 2):
            left_sum += a[i]
            ans = max(ans, left_sum + right_most[i + 2])
        return ans
