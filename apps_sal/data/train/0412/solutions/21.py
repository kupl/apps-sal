class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp_map ={}
        
        for i in range(target):
            dp_map[(1,i+1)] = 0
        for i in range(f):
            dp_map[(1,i+1)] = 1
        
        def recurse_with_mem(d,target):
            
            if (d,target) in dp_map:
                return dp_map[(d,target)]

            if target<=0:
                return 0
            
            num_ways = 0
            for i in range(f):
                num_ways += recurse_with_mem(d-1,target-i-1)
        
            dp_map[(d,target)] = num_ways
            return num_ways
        
        return recurse_with_mem(d,target)%(10**9+7)
