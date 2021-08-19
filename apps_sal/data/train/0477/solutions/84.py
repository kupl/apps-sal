class Solution:

    def findKthBit(self, n: int, k: int) -> str:
        s = '011'
        if k < 4:
            return s[k - 1]
        d = {'0': '1', '1': '0'}
        for i in range(n):
            s += '1'
            if len(s) == k:
                return '1'
            else:
                for x in s[:-1][::-1]:
                    s += d[x]
                    if len(s) == k:
                        return d[x]
