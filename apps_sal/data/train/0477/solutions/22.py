class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s='0'
        for i in range(1,n):
            inv=''
            for j in s:
                if j=='1':
                    inv+='0'
                else:
                    inv+='1'
            s=s+'1'+inv[::-1]
        return s[k-1]

