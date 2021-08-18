class Solution:
    def minSwap(self, A, B):

        return self._dfs(A, B, start=0, swapped=False, memo={})

    def _dfs(self, A, B, start, swapped, memo):
        if start == len(A):
            return 0

        key = (start, swapped)
        if key in memo:
            return memo[key]

        res = 2 ** 31 - 1
        prev_a = A[start - 1] if start > 0 else -2 ** 31 - 1
        prev_b = B[start - 1] if start > 0 else -2 ** 31 - 1

        if A[start] > prev_a and B[start] > prev_b:
            res = min(res, self._dfs(A, B, start + 1, False, memo))

        if A[start] > prev_b and B[start] > prev_a:
            A[start], B[start] = B[start], A[start]
            res = min(res, self._dfs(A, B, start + 1, True, memo) + 1)
            A[start], B[start] = B[start], A[start]

        memo[key] = res
        return res
