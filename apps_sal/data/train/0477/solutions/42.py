class Solution:

    def invert(self, s):
        out = ''
        for c in s:
            if c == '0':
                out += '1'
            if c == '1':
                out += '0'
        return out

    def reverse(self, s):
        return s[::-1]

    def findKthBit(self, n: int, k: int) -> str:
        l = []
        for i in range(n):
            if i == 0:
                l.append('0')
            else:
                last_s = l[-1]
                s = last_s + '1' + self.reverse(self.invert(last_s))
                l.append(s)
        s = l[-1]
        return s[k - 1]
