class Solution:

    def findKthBit(self, n: int, k: int) -> str:
        s2 = '011'
        if k <= 3:
            return s2[k - 1]
        if k == 2 ** (n - 1):
            return '1'
        elif k < 2 ** (n - 1):
            return self.findKthBit(n - 1, k)
        else:
            ans = self.findKthBit(n - 1, 2 ** n - k)
            return '1' if ans == '0' else '0'
