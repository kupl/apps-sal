class Solution:
    def numWays(self, s: str) -> int:
        n = s.count('1')
        m = 10**9+7
        if n%3 != 0:
            return 0
        if n == 0:
            return comb(len(s)-1,2)%m
        n//=3
        
        k = n
        i = 0
        while k:
            if s[i] == '1':
                k-=1
            i+=1
        x = 1
        while s[i] != '1':
            x+=1
            i+=1
        k = n
        while k:
            if s[i] == '1':
                k-=1
            i+=1
        y = 1
        while s[i] != '1':
            y+=1
            i+=1
        return (y*x)%m
