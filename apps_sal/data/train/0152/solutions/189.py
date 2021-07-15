class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        def distance(d):
            p=0 # current position
            c=1 # count of balls put into basket
            while p<len(position)-1:
                
                for i in range(p,len(position)):
                    if position[i]-position[p]>=d:
                        c+=1
                        break
                    
                p=i
                
                if c==m:
                    return True
            return False
        l,r=0,position[-1]
        while l<r:
            md=r-(r-l)//2
            #print(md,distance(md))
            if distance(md):
                l=md
            else:
                r=md-1
        return l
