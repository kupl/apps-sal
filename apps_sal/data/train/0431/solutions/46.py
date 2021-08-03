class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        mod = 10**9 + 7
        left, right = self.PLE(A), self.NLE(A)
        return sum(a * i * j for (a, i, j) in zip(A, left, right)) % mod

    def PLE(self, A):
        n = len(A)
        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and A[stack[-1]] > A[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        for i in range(n):
            left[i] = i + 1 if left[i] == -1 else i - left[i]
        return left

    def NLE(self, A):
        n = len(A)
        right = [-1] * n
        stack = []
        for i in range(n):
            while stack and A[stack[-1]] > A[i]:
                right[stack.pop()] = i
            stack.append(i)

        for i in range(n):
            right[i] = n - i if right[i] == -1 else right[i] - i
        return right
