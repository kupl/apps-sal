def reverse(m):
        t=''
        for i in m:
            if i=='1':
                t=t+'0'
            else:
                t=t+'1'
        return t  
class Solution:      
    def findKthBit(self, n: int, k: int) -> str:
        s='0';
        while(n>1):
            t=reverse(s)
            s=s+'1'+t[::-1]
            n-=1;
        return s[k-1];
