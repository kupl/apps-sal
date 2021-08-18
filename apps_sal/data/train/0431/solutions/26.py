from collections import deque


class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        stack = deque()
        left = [0] * len(A)
        right = [len(A)] * len(A)
        mod = 10**9 + 7

        for i in range(len(A)):
            while stack and A[stack[-1]] > A[i]:
                right[stack[-1]] = i
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        res = 0
        for i in range(len(A)):
            res += A[i] * (i - left[i]) * (right[i] - i)
        return res % mod
