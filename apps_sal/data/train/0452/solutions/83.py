class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        @lru_cache(None)
        def helper(i,d):
            if(d==1):
                if(len(jobDifficulty)==0):
                    return float('inf')
                return max(jobDifficulty[i:])
            else:
                m=float('inf')
                for j in range(i+1,len(jobDifficulty)-d+2):
                    m=min(max(jobDifficulty[i:j])+helper(j,d-1),m)
                return m
        x=helper(0,d)
        if(x==float('inf')):
            return -1
        else:
            return x
            
        

