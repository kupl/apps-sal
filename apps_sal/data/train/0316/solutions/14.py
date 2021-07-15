class Solution:
    def longestPrefix(self, s: str) -> str:
        i,j,l=0,1,len(s)
        m=0
        while(i<l-1):
            if(s[0:i+1]==s[l-i-1: ]):
                m=i+1
                #print(\"i=\",i,s[0:i+1],\" \",s[l-i-1: ])
            i+=1
        if(m==l-1):
            return s[ :l-1]
        else:
            return s[0:m]
                
                

