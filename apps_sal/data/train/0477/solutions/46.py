class Solution:

    def findKthBit(self, n: int, k: int) -> str:

        def inv(s):
            n = ''
            for i in s:
                if i == '1':
                    n += '0'
                else:
                    n += '1'
            return n

        def rev(s):
            return s[::-1]
        s = '0'
        for i in range(n):
            s = s + '1' + rev(inv(s))
        return s[k - 1]
