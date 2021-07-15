class Solution:
    ans=1
    def getans(self,s,start,n,temp):
        self.ans=max(self.ans,len(temp))
        for x in range(start+1,n+1):
            boss=set(list(temp))
            boss.add(s[start:x])
            self.getans(s,x,n,boss)
            
            
    def maxUniqueSplit(self, s: str) -> int:
        temp=set()
        self.getans(s,0,len(s),temp)
        return self.ans
            

