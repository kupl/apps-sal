class Solution(object):

    def sumSubarrayMins(self, A):
        MOD = 10 ** 9 + 7
        n = len(A)
        stack = []
        left = [-1] * n
        for i in range(n):
            while stack and A[i] <= A[stack[-1]]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        stack = []
        right = [n] * n
        for k in range(n - 1, -1, -1):
            while stack and A[k] < A[stack[-1]]:
                stack.pop()
            if stack:
                right[k] = stack[-1]
            stack.append(k)
        return sum(((i - left[i]) * (right[i] - i) * A[i] for i in range(n))) % MOD
