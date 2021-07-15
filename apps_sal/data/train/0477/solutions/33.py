class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        s = ['0']
        for _ in range(n-1):
            s += ['1'] + [('1','0')[int(x)] for x in reversed(s)]
        return s[k-1]

