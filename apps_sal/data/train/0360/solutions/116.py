class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def helper(w):
            i=0
            cnt=0
            while cnt<D:
                curr=0
                while i<len(weights):
                    if curr+weights[i]<=w:
                        curr+=weights[i]
                        i+=1
                    else:
                        break
                cnt+=1
            return False if i!=len(weights) else True
        l,r=max(weights),sum(weights)
        while l<=r:
            mid=(l+r)//2
            if helper(mid):
                r=mid-1
            else:
                l=mid+1
        return l
        
            
            

