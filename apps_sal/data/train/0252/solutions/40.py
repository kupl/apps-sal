
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        stack = []
        for i in range(n + 1):
            l, r = i - ranges[i], i + ranges[i]
            if not stack or (l <= 0 and r >= stack[-1]):
                stack = [r]
            elif l <= stack[-1] < r:
                while len(stack) > 1:
                    prev = stack.pop()
                    if l > stack[-1]:
                        stack.append(prev)
                        break
                stack.append(r)
            if stack[-1] >= n:
                return len(stack)
        return -1


class Solution:
    def minTaps(self, n, A):
        dp = [0] + [n + 2] * n
        for i, x in enumerate(A):
            for j in range(max(i - x + 1, 0), min(i + x, n) + 1):
                dp[j] = min(dp[j], dp[max(0, i - x)] + 1)
        return dp[n] if dp[n] < n + 2 else -1
