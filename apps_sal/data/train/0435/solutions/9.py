class Solution:

    def subarraysDivByK(self, A: List[int], K: int) -> int:
        res = 0
        cs = 0
        seen = collections.Counter({0: 1})
        for i in range(len(A)):
            x = A[i]
            cs += x
            if cs % K in seen:
                res += seen[cs % K]
            seen[cs % K] += 1
        return res
