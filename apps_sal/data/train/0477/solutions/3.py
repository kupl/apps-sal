class Solution:

    def findKthBit(self, n: int, k: int) -> str:

        def invert(s):
            return ''.join(['1' if c == '0' else '0' for c in s])

        def revStr(s):
            return ''.join(list(reversed(s)))
        counter = 1
        x = '0'
        while counter != n:
            x = x + '1' + revStr(invert(x))
            counter += 1
        return x[k - 1]
