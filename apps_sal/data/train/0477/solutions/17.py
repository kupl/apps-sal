class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def reverse(cur_s):
            return ''.join([c for c in reversed(cur_s)])

        def invert(cur_s):
            return ''.join(['1' if c == '0' else '0' for c in cur_s])

        S = '0'
        for i in range(1, n):
            S += '1' + reverse(invert(S))

        return S[k - 1]
