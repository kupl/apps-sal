class Solution:

    def strWithout3a3b(self, A: int, B: int) -> str:
        if A >= B:
            if A >= B * 2:
                return 'aab' * B + 'a' * (A - B * 2)
            return 'aab' * (A - B) + 'ab' * (B * 2 - A)
        if B >= A * 2:
            return 'bba' * A + 'b' * (B - A * 2)
        return 'bba' * (B - A) + 'ba' * (A * 2 - B)
