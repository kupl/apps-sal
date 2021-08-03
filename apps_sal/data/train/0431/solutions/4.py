class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        n = len(A)
        low = [None] * (n)
        high = [None] * (n)
        stack = []

        for i in range(n):
            while stack and A[stack[-1]] >= A[i]:
                stack.pop()

            low[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and A[stack[-1]] > A[i]:
                stack.pop()
            high[i] = stack[-1] if stack else n
            stack.append(i)
        ans = 0
        for i in range(n):
            ans = (ans + (i - low[i]) * (high[i] - i) * A[i]) % int(1e9 + 7)
        return ans
