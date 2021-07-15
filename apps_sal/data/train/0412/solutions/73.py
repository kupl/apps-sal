class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        self.map = collections.defaultdict(int)
        return self.noOfWays(d,f, target)
        
    def noOfWays(self,d, f, target):
           
        if(d==0 and target==0):
            return 1
        elif(d==0):
            return 0

        if((d,target) in self.map):
            return self.map[(d,target)]
        res = 0
        for i in range(1, f+1):
            res+= (self.noOfWays(d-1,f, target-i))
        self.map[(d,target)] = res  
        return res%(10**9 + 7)

