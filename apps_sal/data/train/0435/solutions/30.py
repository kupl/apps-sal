class Solution:

    def subarraysDivByK(self, A: List[int], K: int) -> int:
        (D, s) = ({0: 1}, 0)
        for a in A:
            s = (s + a) % K
            if s in D:
                D[s] += 1
            else:
                D[s] = 1
        return sum((i * (i - 1) // 2 for i in list(D.values())))
