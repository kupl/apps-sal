class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        N = len(A)
        stack = []
        res = 0
        instack = 0
        for i in range(N):
            tmp = 1
            while stack and stack[-1][0] >= A[i]:
                x, cnt = stack.pop()
                tmp += cnt
                instack -= x * cnt
            stack.append((A[i], tmp))
            instack += A[i] * tmp

            res += instack
        return res % (10**9 + 7)
