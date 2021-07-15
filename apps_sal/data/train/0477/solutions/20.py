class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = '0'
        for i in range(1, n):
            chars = []
            for j in reversed(list(range(len(s)))):
                chars.append('1' if s[j] == '0' else '0')
            s += '1' + ''.join(chars)
            # print('i = {0}, s = {1}'.format(i, s))
        return s[k - 1]

