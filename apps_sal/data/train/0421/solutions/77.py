class Solution:
    def lastSubstring(self, s: str) -> str:
        #from itertools import permutations 
        #print(''.join(p) for p in permutations(s))
        i,j,k=0,1,0
        n=len(s)
        while j+k<n:
            
            if s[i+k]==s[j+k]:
                k+=1
                continue
            elif s[i+k]>s[j+k]:
                j=j+k+1
            else:
                i=max(j,i+k+1)
                j=i+1
            k=0
        return s[i:]
