class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def invert(s):
            inv=''
            for ch in s:
                inv+='0' if ch=='1' else '1'
            return inv
        s='0'
        for i in range(1,n):          
            s=s+'1'+invert(s)[::-1]
            
        return s[k-1]

