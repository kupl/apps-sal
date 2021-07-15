class Solution:
    def numSplits(self, s: str) -> int:
        if len(s)==1:
            return 0
        ln=len(s)
        ans=0
        t1={}
        t2={}
        l1,l2=0,0
        t1[s[0]]=1
        for i in range(1,ln):
            if s[i] in list(t2.keys()):
                t2[s[i]]+=1
            else:
                t2[s[i]]=1
                
        if len(list(t1.keys()))==len(list(t2.keys())):
            ans+=1
        for i in range(1,ln):
            if s[i] in list(t1.keys()):
                t1[s[i]]+=1
            else:
                t1[s[i]]=1
            
            t2[s[i]]-=1
            if t2[s[i]]==0:
                del t2[s[i]]
            
            if len(t1)==len(t2):
                ans+=1
            
            
        
        return ans 

