class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        def check(position,m,f):
            
            prev=0
            balls=1
            index=1
            
            while index<len(position) and balls<=m:
                if position[index]-position[prev]>=f:
                    prev=index
                    index+=1
                    balls+=1
                else:
                    index+=1
            
            if balls>=m:
                return True
            else:
                return False
            
        position=sorted(position)
        start=1
        end=max(position)
        
        
        while start<end:
            mid=(start+end)//2
            
            if check(position,m,mid):
                start=mid+1
            else:
                end=mid
        
        return start-1
