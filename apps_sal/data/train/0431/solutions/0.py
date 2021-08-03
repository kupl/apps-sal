class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        stack = []
        result = 0
        A = [0] + A + [0]

        for i, x in enumerate(A):
            while stack and x < A[stack[-1]]:
                j = stack.pop()
                result += A[j] * (i - j) * (j - stack[-1])
            stack.append(i)

        return result % (10**9 + 7)
