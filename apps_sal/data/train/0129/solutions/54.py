class Solution:
    def maxScoreSightseeingPair(self, a: List[int]) -> int:
        d=[]
        
        for i in range(len(a)-1,-1,-1):
            if i!=0:
                d.append([a[i]-i,i])
        d.sort()
        s=0
        for i in range(0,len(a)-1):
            while d[-1][1]<=i:
                d.pop()
        
            s=max(s,a[i]+i+d[-1][0])
        return s
            
            
        
            
        
        
        
        
            

