class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        if len(A) <= 1:
            return len(A)

        memo = [2 * [1] for _ in range(len(A) + 1)]
        res = 1

        for i in range(1, len(A)):
            for sign in range(2):
                if A[i] != A[i - 1] and int(A[i] > A[i - 1]) == sign:
                    memo[i][sign] = max(memo[i][sign], 1 + memo[i - 1][(sign + 1) % 2])
                    res = max(res, memo[i][sign])

        return res
