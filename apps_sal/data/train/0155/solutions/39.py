class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [1] * (n + 1)
        stack = []
        for (i, a) in enumerate(arr + [float('inf')]):
            while stack and arr[stack[-1]] < a:
                last = [stack.pop()]
                while stack and arr[stack[-1]] == arr[last[0]]:
                    last.append(stack.pop())
                for j in last:
                    if i - j <= d:
                        dp[i] = max(dp[i], dp[j] + 1)
                    if stack and j - stack[-1] <= d:
                        dp[stack[-1]] = max(dp[stack[-1]], dp[j] + 1)
            stack.append(i)
        return max(dp[:-1])
