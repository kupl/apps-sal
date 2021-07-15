class Solution:
    def longestPrefix(self, s: str) -> str:
        lps=[0]*len(s)
        i=1
        l=0
        while(i<len(s)):
            if(s[i]==s[l]):
                l=l+1
                lps[i]=l
                i=i+1
            else:
                if(l):
                    l=lps[l-1]
                else:
                    lps[i]=0
                    i=i+1
        m=lps[-1]
        index=len(s)-1
        #print(lps)
        #for i in range(len(s)):
         #   if(lps[i]>m):
          #      m=lps[i]
           #     index=i
        
        #print(m,index)
        return s[abs(m-index-1):index+1]
