class Solution:
    def numWays(self, s: str) -> int:
        f = [0,0]
        ind,curr = 0,0
        target = 0
        for i in s: target+=1 if i=='1' else 0
        if target%3:
            return 0
        target = target//3
        n=len(s)
        if target == 0:
            return (math.factorial(n-1)//(math.factorial(2)*math.factorial(n-3)))%(10**9+7)
        for i in range(len(s)):
            if s[i]=='1':
                curr+=1
                if ind==1 or ind==3:
                    ind+=1
            elif ind==1 or ind==3:
                f[(ind-1)//2]+=1
            if curr==target:
                ind+=1
                curr=0
        return ((f[0]+1)*(f[1]+1))%(10**9+7)
