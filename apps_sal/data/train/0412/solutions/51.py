class Solution:
    
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        
        #[1,2,3,4,5,6], target=7
        #[1,2,3,4,5,6]
        #[1,2,3,4,5,6]
        #[]
        
        store = {}
        
        def helper(d, f, target):
            if d==0 or f==0 or target<=0:
                return 0
            if d==1 and target>f:
                return 0
            if d==1 and target<=f:
                return 1
        
            if (d, f, target) in store:
                 return store[(d,f,target)]
        
            n = 0
            for i in range(1, f+1):
                n += helper(d-1, f, target-i)
        
            store[(d, f, target)] = n
            return n
    
        #d=2, f=6, t=7
        #i=1, 1,6,6
        
        return (helper(d, f, target))%(10**9 + 7)
            
        #2,6,7
        #(1,6,6), (1,6,5), (1,6,4), (1,6,3), (1,6,2),(1,6,1)
        

