from copy import deepcopy


def cumsum(A: list) -> list:
    cum = 0
    res = []
    for x in A:
        cum += x
        res.append(cum)
    return res


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        opt = deepcopy(A)
        n = len(A)

        for i in range(1, n, 1):
            if opt[i - 1] + A[i] > opt[i]:
                opt[i] = opt[i - 1] + A[i]

        forward_cumsum = cumsum(A)

        back_cumsum = cumsum(A[::-1])
        tmp = [back_cumsum[0]]
        for i in range(1, n):
            tmp.append(max(tmp[i - 1], back_cumsum[i]))
        back_cumsum = tmp

        for i in range(0, n - 1):
            potential_replacement = forward_cumsum[i] + back_cumsum[(n - 2) - i]
            opt[i] = max(opt[i], potential_replacement)

        return max(opt)
