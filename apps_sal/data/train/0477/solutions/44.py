class Solution:

    def findKthBit(self, n: int, k: int) -> str:
        s0 = '0'
        i = 1
        while i <= n:
            s0 = s0 + '1' + self.reverse(s0)
            i = i + 1
        return s0[k - 1]

    def reverse(self, s):
        mapp = {'1': '0', '0': '1'}
        ans = ''
        for x in s:
            ans = ans + mapp[x]
        return ans[::-1]
