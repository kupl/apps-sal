class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def reverse(s):
            return ''.join([s[len(s) - 1 - i] for i in range(len(s))])

        def invert(s):
            return ''.join(['1' if s[i] == '0' else '0' for i in range(len(s))])

        def findNthStr(n1):
            if n1 == 1:
                return '0'
            else:
                prev = findNthStr(n1 - 1)
                return prev + '1' + reverse(invert(prev))

        return findNthStr(n)[k - 1]
