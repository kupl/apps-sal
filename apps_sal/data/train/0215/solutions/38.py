class Solution:

    def isGoodArray(self, A: List[int]) -> bool:
        if len(A) == 0:
            return False
        gcd = A[0]
        for a in A:
            while a:
                (gcd, a) = (a, gcd % a)
        return gcd == 1
