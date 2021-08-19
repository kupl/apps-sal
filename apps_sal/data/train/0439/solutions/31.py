class Solution:

    def maxTurbulenceSize(self, A: List[int]) -> int:
        if not A:
            return 0
        if len(A) == 1:
            return 1
        n = len(A)
        res = [1] * n
        res_max = 1
        for i in range(1, n):
            if A[i] == A[i - 1]:
                res[i] = 1
            elif A[i] < A[i - 1]:
                if i == 1:
                    res[i] = 2
                elif A[i - 1] <= A[i - 2]:
                    res[i] = 2
                else:
                    res[i] = res[i - 1] + 1
            elif i == 1:
                res[i] = 2
            elif A[i - 1] >= A[i - 2]:
                res[i] = 2
            else:
                res[i] = res[i - 1] + 1
            res_max = max(res_max, res[i])
        print(res)
        return res_max
