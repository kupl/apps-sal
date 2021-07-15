class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def build_string(n):
            previous = '0'

            for i in range(1, n):
                invert = ''
                for c in previous:
                    if c == '1':
                        invert += '0'
                    else:
                        invert += '1'
                previous = previous + '1' + invert[::-1]
            return previous

        ans = build_string(n)
        return ans[k-1]
