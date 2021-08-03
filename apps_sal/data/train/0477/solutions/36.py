class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        k -= 1

        s = '0'
        i = 0
        while i < n:
            inverted = ''.join('1' if c == '0' else '0' for c in s)[::-1]
            s = s + '1' + inverted
            i += 1

        return s[k]
