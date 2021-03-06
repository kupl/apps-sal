class Solution:

    def sumSubarrayMins(self, A: List[int]) -> int:
        res = 0
        stack = []
        A = [float('-inf')] + A + [float('-inf')]
        for (i, n) in enumerate(A):
            while stack and A[stack[-1]] > n:
                cur = stack.pop()
                res += A[cur] * (cur - stack[-1]) * (i - cur)
            stack.append(i)
        return res % (10 ** 9 + 7)
