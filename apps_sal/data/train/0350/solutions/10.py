class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        start = 0
        first_uni = 0
        re = 0
        dd = {}
        
        for i, cur in enumerate(A):
            dd[cur]  = dd.get(cur, 0) + 1
            
            if len(dd) == K + 1:
                dd.pop(A[first_uni])
                first_uni += 1
                start = first_uni
            
            if len(dd) == K:
                while first_uni <= i and dd[A[first_uni]] != 1:
                    dd[A[first_uni]] -= 1
                    first_uni += 1
                re += first_uni - start +1
        
        return re



