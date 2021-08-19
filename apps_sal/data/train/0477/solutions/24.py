class Solution:

    def findKthBit(self, n: int, k: int) -> str:

        def invert(s):
            temp = ''
            for i in range(len(s)):
                if s[i] == '1':
                    temp = temp + '0'
                else:
                    temp = temp + '1'
            return temp
        s = '0'
        for i in range(1, n):
            inv = invert(s)
            rev = inv[::-1]
            s = s + '1' + rev
        return s[k - 1]
