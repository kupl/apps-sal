class Solution:

    def findKthBit(self, n: int, k: int) -> str:
        s = '0'
        while n > 1:
            p = ''
            for l in s[::-1]:
                p += '1' if l == '0' else '0'
            s = s + '1' + p
            n -= 1
        return s[k - 1]
