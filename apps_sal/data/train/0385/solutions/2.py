class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        i = 1
        # factors that are smaller than sqrt(n)
        factor_list_small = []
        # factors that are larger than sqrt(n)
        factor_list_large = []
        while pow(i, 2) < n:
            a, b = divmod(n, i)  # a is the quotient, b is the remainder
            if b == 0:
                factor_list_small.append(i)  # add to the end
                factor_list_large = [a] + factor_list_large  # add to the beginning
            i += 1
        if pow(i, 2) == n:
            factor_list_small.append(i)
        # combine these two lists together
        factor_list = factor_list_small + factor_list_large
        if len(factor_list) < k:
            return(-1)
        else:
            return(factor_list[k - 1])
