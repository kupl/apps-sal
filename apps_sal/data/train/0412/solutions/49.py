class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        return self.recurse(d,0,f,0,target,{})%(10**9+7)
    
    def recurse(self,dices,dno,faces,cursum,target,cache):
        if cursum>target:
            return 0
        
        if dno==dices:
            if cursum==target:
                return 1
            return 0
        
        if (dno,cursum) in cache:
            return cache[(dno,cursum)]
        
        ways=0
        for curface in range(1,faces+1):
            ways+=self.recurse(dices,dno+1,faces,cursum+curface,target,cache)
        cache[(dno,cursum)]=ways
        return ways
