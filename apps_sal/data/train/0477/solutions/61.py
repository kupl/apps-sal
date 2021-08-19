class Solution:

    def findKthBit(self, n: int, k: int) -> str:

        def operator(s):
            t = reversed(['0' if i == '1' else '1' for i in s])
            return s + '1' + ''.join(t)
        s = '0'
        while len(s) < k:
            s = operator(s)
        return s[k - 1]
