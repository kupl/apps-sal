class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = '0'
        if n == 1:
            return '0'
        for i in range(1, n):
            s_i = s[::-1]
            s = s + '1' + ''.join(['1' if c == '0' else '0' for c in s_i])
        return s[k - 1]
