class Solution:
    
        
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def f(mid,position,m):
            f=position[0]
            m=m-1
            for j in range(1,len(position)):
                if position[j]-f>=mid:
                    f=position[j]
                    m=m-1
                if m<0:
                    break
            if m<=0:
                return True
            return False
        h=(position[-1]-position[0])//(m-1)+1
        l=0
        while h>=l:
            mid=(h+l)//2
            
            print(mid)
            if f(mid,position,m):
                l=mid+1
            else:
                h=mid-1
        return l-1
