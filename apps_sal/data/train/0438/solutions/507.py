class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        import numpy as np

        def max_rolling1(a, window, axis=1):
            shape = a.shape[:-1] + (a.shape[-1] - window + 1, window)
            strides = a.strides + (a.strides[-1],)
            rolling = np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)
            return np.max(rolling, axis=axis)

        n = len(arr)
        L = [0] * n
        for i in range(n):
            L[arr[i] - 1] = i

        A = np.array(L)
        K = m
        RM = (max_rolling1(A, K))
        hh = -1
        if m == n:
            return n
        for i in range(n - m + 1):
            temp = [L[x] for x in [i - 1, i + m] if x in range(n)]

            if min(temp) > RM[i]:
                hh = max(hh, min(temp))
        return hh
