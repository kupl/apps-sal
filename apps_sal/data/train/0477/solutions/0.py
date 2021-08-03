class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        i = n - 1
        invert = False
        while i > 0:
            half_len = (2**(i + 1) - 1) // 2
            if k == half_len + 1:
                return '1' if not invert else '0'

            if k > half_len:
                k = half_len - (k - half_len - 1) + 1
                invert = not invert
            i -= 1

        return '1' if invert else '0'
