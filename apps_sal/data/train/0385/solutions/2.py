class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        i = 1
        factor_list_small = []
        factor_list_large = []
        while pow(i, 2) < n:
            a, b = divmod(n, i)
            if b == 0:
                factor_list_small.append(i)
                factor_list_large = [a] + factor_list_large
            i += 1
        if pow(i, 2) == n:
            factor_list_small.append(i)
        factor_list = factor_list_small + factor_list_large
        if len(factor_list) < k:
            return(-1)
        else:
            return(factor_list[k - 1])
