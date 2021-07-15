class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = '0'
        inv = '1'
        rev_inv = '1'
        
        for i in range(n-1):
            s = s + '1' + rev_inv
            inv = ''
            rev_inv = ''
            for j in range(len(s)):
                if s[j]=='0':
                    inv+='1'
                else:
                    inv+='0'
            rev_inv = inv[::-1]
            
        return s[k-1]
