class Solution:

    def findKthBit(self, n: int, k: int) -> str:
        s = ''

        def recurse(n):
            nonlocal s
            if n <= 1:
                return '0'
            else:
                _str = recurse(n - 1)
                s = _str + '1' + self.reverse(self.invert(_str))
                return s
        return recurse(n)[k - 1]

    def invert(self, string):
        return ''.join(['0' if char == '1' else '1' for char in string])

    def reverse(self, string):
        return string[::-1]
