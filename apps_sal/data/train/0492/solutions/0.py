class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        if A >= 2*B:
            return 'aab'* B + 'a'* (A-2*B)
        elif A >= B:
            return 'aab' * (A-B) + 'ab' * (2*B - A)
        elif B >= 2*A:
            return 'bba' * A + 'b' *(B-2*A)
        else:
            return 'bba' * (B-A) + 'ab' * (2*A - B)
