class Solution:

    def sumSubarrayMins(self, A: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(A)
        stack = []
        left = [None] * n
        for i in range(n):
            while stack and A[i] <= A[stack[-1]]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            else:
                left[i] = -1
            stack.append(i)
        stack = []
        right = [n] * n
        for i in range(n):
            while stack and A[i] <= A[stack[-1]]:
                right[stack.pop()] = i
            stack.append(i)
        res = 0
        for i in range(n):
            res += (i - left[i]) * (right[i] - i) * A[i]
        return res % MOD
