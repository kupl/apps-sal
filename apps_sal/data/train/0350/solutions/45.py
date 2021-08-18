from collections import defaultdict as dd


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        n = len(A)
        i = j = 0
        d = dd(int)
        res = 0
        while j < n:
            while j < n and len(d) < K:
                d[A[j]] += 1
                j += 1
            i1, j1 = i, j
            d[A[i]] -= 1
            while d[A[i]] > 0:
                i += 1
                d[A[i]] -= 1
            while j < n and A[j] in d:
                j += 1
            if len(d) == K:
                res += (i - i1 + 1) * (j - j1 + 1)
            d.pop(A[i])
            i += 1
            j = j1
        return res
