class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        #6:00
        # if we have 1 one egg
        # we will need N attempts
        
        # if we have 2 egg
        # pick start postion as any k
        # if it breaks
        # then we will need f(k-1,1)
        # if it doesn't break f(n-k+1,2)
        @lru_cache(None)
        def helper(floors,eggs):
            if floors<=0:return 0
            if eggs==1:return floors
            # pick k
            ans=floors
            low,high=1,floors
            while low+1<high:
                # we dont low, high to be together
                mid=low+(high-low)//2
                t1=helper(mid-1,eggs-1)
                t2=helper(floors-mid,eggs)
                if t1<t2:
                    low=mid
                elif t1>t2:
                    high=mid
                else:
                    low=high=mid
            ans=floors
            for k in (low,high):
                ans=min(ans,1+max(helper(k-1,eggs-1),helper(floors-k,eggs)))
                
                
            
#             for k in range(1,floors+1):
#                 # can it be binary search? i think graph has to be symmetric
                
#                 ans=min(ans,1+max(helper(k-1,eggs-1),helper(floors-k,eggs)))
            return ans
        return helper(N,K)
        
        
        
        
        
        
        

