class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mem = {(0, 0): 1}
        def find(d: int, target: int):
            if (d, target) in mem:
                return mem[(d, target)]
            
            if d == 0:
                return 0
            
            res = 0
            d -= 1
            for i in range(1, min(target - d, f)+1):
                res += find(d, target-i)
            mem[(d+1, target)] = res
            return res
        
        return find(d, target) % (10**9 + 7)

