class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n==1:
            return '0'
        def rev(s):
            return s[::-1]
        def invert(r):
            t=''
            for i in r:
                if i=='1':
                    t+='0'
                else:
                    t+='1'
            return t
        z='0'
        for i in range(2,n+1):
            a=invert(z)
            b=rev(a)
            z+='1'+b
        return z[k-1]
            
            

