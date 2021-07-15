class Solution:
    
    def dfs(self, pos):
        if pos==self.n:
            self.ans += 1
            return
        
        last = None
        for i, val in enumerate(self.a):
            if self.usable[i]:
                if val == last:
                    continue
                if pos-1 >= 0 and (val + self.rec[pos-1]) not in self.square:
                    continue
                
                self.usable[i] = False
                self.rec[pos] = val
                self.dfs(pos + 1)
                self.usable[i] = True
                last = val
    
    def numSquarefulPerms(self, A: List[int]) -> int:
        
        self.a = sorted(A)
        self.square=set()
        i = 0 # not 1
        while i*i <= self.a[-1]*2:
            self.square.add(i*i)
            i += 1
        
        #print(self.square)
        self.ans = 0
        self.n = len(self.a)       
        self.usable = [True]*self.n
        self.rec = [None]*self.n
        self.dfs(0)
        return self.ans
        
        
        

