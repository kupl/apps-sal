class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i=0
        j=0
        cur_max=0
        maxx=0
        for i in range(len(s)):
            if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
                cur_max+=1
            if i-j+1>k:
                if s[j]=='a' or s[j]=='e' or s[j]=='i' or s[j]=='o' or s[j]=='u':
                    cur_max-=1
                maxx=max(cur_max,maxx)
                j+=1
            maxx=max(cur_max,maxx)
        return maxx
                
            
            
            
            

