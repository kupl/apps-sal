class Solution:
    def numWays(self, s: str) -> int:
        prefix = [0 for i in range(len(s))]
        for i in range(len(s)):
            if(s[i] == '1'):
                if(i == 0):
                    prefix[i] = 1
                else:
                    prefix[i] = 1 + prefix[i-1]
            else:
                if(i!=0):
                    prefix[i] = prefix[i-1]
        if(prefix[-1] == 0):
            return(((len(s)-2)*(len(s)-1)//2)%(10**9+7))
        elif(prefix[-1]%3!=0):
            return(0)
        else:
            c1 = 0
            c2 = 0
            for i in range(len(prefix)):
                if(prefix[i] == prefix[-1]//3):
                    c1+=1
                elif(prefix[i] == 2*prefix[-1]//3):
                    c2+=1
            return((c1*c2)%(10**9+7))
                

