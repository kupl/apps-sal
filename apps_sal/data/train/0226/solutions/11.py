import numpy as np
class Solution:
    graph = {}
    count = {}
    def numSquarefulPerms(self, A: List[int]) -> int:
        self.graph = {}
        self.count = {}
        for i in A:
            if i in self.count:
                self.count[i] += 1
            else:
                self.count[i] = 1
            self.graph[i] = []
            
        for i in self.count:
            for j in self.count:
                r = int(np.sqrt(i + j))
                if r * r == i + j:
                    self.graph[i].append(j)
        ans = 0
        L = len(A)
        print((self.count))
        print((self.graph))
        for i in self.graph:
            ans += self.dfs(i, L-1)
        return ans
    
    def dfs(self, i, L):
        self.count[i] -= 1
        ans = 1
        if L != 0:
            ans = 0
            for j in self.graph[i]:
                if self.count[j] != 0:
                    ans += self.dfs(j, L - 1)
        self.count[i] += 1
        return ans
    

