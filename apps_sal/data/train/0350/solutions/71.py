class Solution:

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        dd = {}
        first_uni = 0
        start = 0
        re = 0
        for i in range(len(A)):
            dd[A[i]] = dd.get(A[i], 0) + 1
            if len(dd) == K + 1:
                dd.pop(A[first_uni])
                first_uni += 1
                start = first_uni
            if len(dd) == K:
                while dd[A[first_uni]] > 1:
                    dd[A[first_uni]] -= 1
                    first_uni += 1
                re += first_uni - start + 1
        return re
