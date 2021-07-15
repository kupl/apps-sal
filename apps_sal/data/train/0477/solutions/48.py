class Solution:
    def invert(self, t):
        ret = ''
        for i in t:
            if i == '0':
                ret += '1'
            else:
                ret += '0'
        return ret
    
    def findKthBit(self, n: int, k: int) -> str:
        i = 1
        l = list()
        l.append('0')
        while i <= n:
            t = l[-1]
            ans = t + '1' 
            ans += self.invert(t[::-1])
            l.append(ans)
            i += 1
        return l[-1][k - 1]
            
            

