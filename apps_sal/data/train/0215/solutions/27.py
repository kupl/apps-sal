class Solution:
    def isGoodArray(self, A: List[int]) -> bool:
        gcd = A[0]
        for a in A:
            while a:
                gcd, a = a, gcd % a
                if gcd == 1:
                    return gcd
        return False
