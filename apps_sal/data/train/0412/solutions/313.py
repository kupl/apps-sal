class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if not d or not f or target == 0:
            return 0
            
        def dfs(d, f, hash_map, target):
            
            
            if target == 0 and d == 0:
                return 1
            if target<=0 or target>d*f or target<d:
                return 0
            
            # logic
            if (d,target) in hash_map:
                return hash_map[(d,target)]
            
            cnt = 0
            for i in range(1, f+1):
                if target-i<0:
                    break
                cnt += dfs(d-1, f,hash_map, target-i)
                cnt %= 1000000007

            hash_map[(d,target)] = cnt
            return hash_map[(d,target)]
        
        return dfs(d,f,{},target)
    

  
    

        

