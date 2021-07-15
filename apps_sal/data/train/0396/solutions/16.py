class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if(K%2==0 or K%5==0):return -1
        l = len(str(K))
        n = int(''.join(['1']*l))
        while(True):
            if(n%K==0):return l
            n=(n*10)+1
            l+=1
        return -1
        

