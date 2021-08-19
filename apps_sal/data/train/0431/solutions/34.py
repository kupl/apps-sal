class Solution:

    def sumSubarrayMins(self, A: List[int]) -> int:
        N = len(A)
        stack = []
        (left, right) = ([None] * N, [None] * N)
        for i in range(N):
            while stack and A[i] <= A[stack[-1]]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        stack.clear()
        for i in range(N - 1, -1, -1):
            while stack and A[i] < A[stack[-1]]:
                stack.pop()
            right[i] = stack[-1] if stack else N
            stack.append(i)
        count = 0
        for i in range(N):
            count += (i - left[i]) * (right[i] - i) * A[i]
        return count % (10 ** 9 + 7)
