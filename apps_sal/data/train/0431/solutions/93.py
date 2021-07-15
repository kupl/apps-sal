class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        res, stack, MOD = 0, [], 10**9 + 7
        for i, x in enumerate(A):
            while stack and A[stack[-1]] >= x:
                idx = stack.pop()
                left = stack[-1] if stack else -1
                res += A[idx] * (idx - left) * (i - idx) % MOD
            stack.append(i)
        while stack:
            idx = stack.pop()
            left = stack[-1] if stack else -1
            res += A[idx] * (idx - left) * (len(A) - idx) % MOD
        return res % MOD
