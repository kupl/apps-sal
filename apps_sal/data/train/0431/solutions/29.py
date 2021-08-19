class Solution:

    def sumSubarrayMins(self, A: List[int]) -> int:
        mod = 10 ** 9 + 7
        (left, right) = self.findFirstSmaller(A)
        ans = 0
        for i in range(len(A)):
            ans += A[i] % mod * ((right[i] - 1 - i + 1) * (i - (left[i] + 1) + 1)) % mod
        return ans % mod

    def findFirstSmaller(self, A):
        (left, right) = ([-1] * len(A), [len(A)] * len(A))
        stack = []
        for (i, n) in enumerate(A):
            while stack and stack[-1][0] > n:
                right[stack.pop()[1]] = i
            if stack:
                left[i] = stack[-1][1]
            stack.append((n, i))
        return (left, right)
