class Solution:
    def numWays(self, s: str) -> int:
        count = 0
        dic = {}
        M = 10**9+7
        n = len(s)
        for i in range(n):
            if s[i]=='1':
                count+=1
                dic[count] = i
        if count%3 != 0:
            return 0
        if count == 0:
            return int((n-1)*(n-2)/2%M)
        
        x = dic[count/3+1]-dic[count/3]
        y = dic[2*count/3+1]-dic[2*count/3]
        
        return x*y%M
