class Solution:

    def findKthBit(self, n: int, k: int) -> str:
        switch = {'0': '1', '1': '0'}
        s = '0'
        while len(s) < k:
            s = s + '1' + ''.join((switch[i] for i in reversed(s)))
        return s[k - 1]
