class Solution:
    max_=0
    def maxUniqueSplit(self, s: str) -> int:
        b=len(s)-1
        ar=[]
        self.h(s,b,ar)
        return self.max_
    def h(self,s,b,ar):
        ar2=ar.copy()
        if(b<0):
            self.max_=max(self.max_,len(ar2))
            return 0
        t=s[b:]
        self.h(s,b-1,ar2)
        s=s[:b]
                
        if(t not in ar2):
            ar2.append(t)
            self.h(s,b-1,ar2)
    

