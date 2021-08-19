class Solution:

    def sumSubarrayMins(self, A: List[int]) -> int:
        mod = 10 ** 9 + 7
        left = [-1] * len(A)
        right = [len(A)] * len(A)
        stack = [0]
        for i in range(1, len(A)):
            if A[i] > A[stack[-1]]:
                left[i] = stack[-1]
            else:
                while stack and A[i] <= A[stack[-1]]:
                    stack.pop()
                if not stack:
                    left[i] = -1
                else:
                    left[i] = stack[-1]
            stack.append(i)
        stack = [len(A) - 1]
        for i in range(len(A) - 2, -1, -1):
            if A[i] > A[stack[-1]]:
                right[i] = stack[-1]
            else:
                while stack and A[i] < A[stack[-1]]:
                    stack.pop()
                if not stack:
                    right[i] = len(A)
                else:
                    right[i] = stack[-1]
            stack.append(i)
        res = 0
        for i in range(len(A)):
            res += A[i] * (i - left[i]) * (right[i] - i)
        return res % mod
