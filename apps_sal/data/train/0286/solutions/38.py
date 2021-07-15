class Solution:
    def getProbability(self, balls: List[int]) -> float:
        self.n = len(balls)
        self.mem = {0: 1}
        self.mem2 = {}
        self.balls = balls
        rv = self.dfs(0, [], [])
        #print(self.mem2, self.mem)
        return rv / self.multinomial(balls)
        
        
    def dfs(self, idx, lefts, rights):
        if idx >= self.n:
            if not lefts or not rights:
                return 0
            if len(lefts) != len(rights):
                return 0
            if sum(lefts) != sum(rights):
                return 0
            return self.multinomial(lefts)*self.multinomial(rights)
        
        rv = 0
        for i in range(0, self.balls[idx]+1):
            x1 = i
            x2 = self.balls[idx] - x1
            if x1 == 0:
                rights.append(x2)
                rv += self.dfs(idx+1, lefts, rights)
                rights.pop()
            elif x2 == 0:
                lefts.append(x1)
                rv += self.dfs(idx+1, lefts, rights)
                lefts.pop()
            else:
                lefts.append(x1)
                rights.append(x2)
                rv += self.dfs(idx+1, lefts, rights)
                rights.pop()
                lefts.pop()
        return rv

        
    def multinomial(self, arr):
        if not arr:
            return 0
        arr = arr[:]
        arr.sort()
        key = tuple(arr)
        if key in self.mem2:
            return self.mem2[key]
        
        res = self.frac(sum(arr))
        for x in arr:
            res //= self.frac(x)
        self.mem2[key] = res
        return res

    
    def frac(self, x):
        if x in self.mem:
            return self.mem[x]
        rv =  x * self.frac(x-1)
        self.mem[x] = rv
        return rv
