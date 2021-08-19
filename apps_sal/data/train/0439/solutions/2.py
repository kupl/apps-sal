class Solution:

    def maxTurbulenceSize(self, A: List[int]) -> int:
        if len(A) <= 1:
            return len(A)
        memo = [2 * [1] for _ in range(len(A) + 1)]
        res = 1
        for i in range(len(A) - 1):
            for sign in range(2):
                if A[i + 1] == A[i]:
                    continue
                if int(A[i + 1] > A[i]) == sign:
                    memo[i + 1][sign] = max(memo[i + 1][sign], memo[i][(sign + 1) % 2] + 1)
                    res = max(res, memo[i + 1][sign])
        return res
