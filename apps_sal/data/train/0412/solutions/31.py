class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        self.dic = {}
        self.f = f
        return self.dfs(d, target) % (10**9 + 7)
        
        
    def dfs(self, dices, tar):
        if (dices, tar) in self.dic:
            return self.dic[(dices, tar)]
        elif tar < 0:
            return 0
        elif dices == 1 and tar <= self.f:
            return 1
        elif dices == 1:
            return 0
        else:
            r = 0
            for i in range(1, min(self.f+1, tar)):
                r += self.dfs(dices-1, tar-i)
            
            self.dic[(dices, tar)] = r
            return r

