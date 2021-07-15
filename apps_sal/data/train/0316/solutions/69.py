class Solution:
    def longestPrefix(self, st: str) -> str:
        a=st
        l=len(a)
        leng=0
        i=1
        lps=[0]
        while i<l:
            if a[leng]==a[i]:
                leng+=1
                lps.append(leng)
                i+=1
            else:
                if leng>0:
                    leng=lps[leng-1]
                else:
                    lps.append(0)
                    i+=1
        return st[:lps[-1]]
