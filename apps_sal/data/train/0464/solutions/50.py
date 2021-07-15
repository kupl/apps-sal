class Solution:
    def minOperations(self, n: int) -> int:
        ans=0
        tot=0
        arr=[]
        for i in range(n):
            arr.append((2*i)+1)
            tot+=((2*i)+1)
        tot=tot//n
        for i in arr:
            if(i<tot):
                ans+=(tot-i)
        return ans
