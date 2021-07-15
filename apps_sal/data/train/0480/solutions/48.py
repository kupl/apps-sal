class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        return self.getWays(0, steps, 0, arrLen, {})
        
        
    def getWays(self, step, steps, position, arrLen, cache):
        if step == steps: return position == 0
        if (step, position) in cache: return cache[(step, position)]
        numWays = 0
        if position > 0:
            numWays += self.getWays(step + 1, steps, position - 1, arrLen, cache)
        if position < arrLen - 1:
            numWays += self.getWays(step + 1, steps, position + 1, arrLen, cache)
        numWays += self.getWays(step + 1, steps, position, arrLen, cache)
        cache[(step, position)] = numWays
        return numWays % (10**9 + 7)
        

