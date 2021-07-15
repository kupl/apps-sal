class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        sn = ['0']
        for i in range(1, n):
            nx = sn[i-1] + '1' + self.reverse(self.invert(sn[i-1]))
            sn.append(nx)
        return sn[-1][k-1]
    
    def invert(self, s):
        return ''.join('0' if _ == '1' else '1' for _ in s)
    
    def reverse(self, s):
        return ''.join(reversed(s))
