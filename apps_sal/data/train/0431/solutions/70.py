MOD = 1000000007
class Solution:
    def sumSubarrayMins(self, A):
        A = [0] + A + [0]
        stack = []
        res = 0
        for right in range(len(A)):
            while stack and A[stack[-1]] > A[right]:
                mid = stack.pop()
                left = stack[-1]
                res += A[mid] * (mid - left) * (right - mid)
                res %= MOD
            stack.append(right)
        return res
