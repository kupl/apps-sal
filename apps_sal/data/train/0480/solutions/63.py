class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        self.arrLen = arrLen
        self.memo = {}
        return self.helper(steps, 0)
    
    def helper(self, steps, pos):
        if (steps, pos) in self.memo:
            return self.memo[(steps, pos)]
        if pos < 0 or pos >= self.arrLen or steps < 0:
            self.memo[(steps, pos)] = 0
            return 0
        if steps == 0:
            if pos == 0:
                self.memo[(steps, pos)] = 1
                return 1
            else:
                self.memo[(steps, pos)] = 0
        res = 0
        for x in [-1, 0, 1]:
            res += self.helper(steps-1, pos+x)
        self.memo[(steps, pos)] = res
        return res % (10**9 + 7)
        

