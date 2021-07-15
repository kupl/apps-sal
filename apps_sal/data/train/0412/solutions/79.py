class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        self.cache = {}    
        return self.helper(0, 0, d, f, target) % (10**9 + 7)
    
    def helper(self, currD, currSum, d, f, target):
        if currD == d:
            return currSum == target
        
        if currD in self.cache and currSum in self.cache[currD]:
            return self.cache[currD][currSum]
        
        ways = 0
        for i in range(1, f+1):
            ways += self.helper(currD+1, currSum + i, d, f, target)
        
        if currD not in self.cache:
            self.cache[currD] = {}
        self.cache[currD][currSum] = ways
        return ways
