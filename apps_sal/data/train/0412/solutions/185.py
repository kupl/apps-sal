class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        
        if d*f < target or d > target:
            return 0
        
        prev = {0:1}
        
        for x in range(d):
            curr = {}
            for y in range(1,f+1):
                
                for prev_sum,count in list(prev.items()):
                    curr_sum = prev_sum+y
                    if curr_sum <= target:
                        curr[curr_sum] = curr.get(curr_sum,0)+count
            prev = curr
            # print(prev)
        return prev[target]%(10**9+7) if target in prev else 0

