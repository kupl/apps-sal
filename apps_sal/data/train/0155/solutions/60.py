class Solution:
    def maxJumps(self, A: List[int], d: int) -> int:
        n = len(A)
        dp = [1] * (n + 1)
        stack = []
        for i, a in enumerate(A + [float('inf')]):
            while stack and A[stack[-1]] < a:
                L = [stack.pop()]
                while stack and A[stack[-1]] == A[L[0]]:
                    L.append(stack.pop())
                for j in L:
                    if i - j <= d:
                        dp[i] = max(dp[i], dp[j] + 1)
                    if stack and j - stack[-1] <= d:
                        dp[stack[-1]] = max(dp[stack[-1]], dp[j] + 1)
            stack.append(i)
        return max(dp[:-1])
