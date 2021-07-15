class Solution:
    def lastSubstring(self, s: str) -> str:
        if len(set(s))==1:
            return s
        alpha=sorted(list(set(s)))
        start=alpha[-1]
        
        n=len(s)
        index=[]
        for i,char in enumerate(s):
            if char==start:
                index.append(i)
            
        prefix=start
        maxprefix=start
        while index:
            nextindex=[]
            for i in index:
                if i+1<n:
                    if prefix+s[i+1]==maxprefix:
                        maxprefix=prefix+s[i+1]
                        nextindex.append(i+1)
                    elif prefix+s[i+1]>maxprefix:
                        maxprefix=prefix+s[i+1]
                        nextindex=[i+1]
            prefix=maxprefix
            index=nextindex
        
        return maxprefix
                    

