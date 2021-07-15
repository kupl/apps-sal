class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:
        n = len(A)
        self.cost = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                w1 = A[i]
                w2 = A[j]
                k = min(len(w1), len(w2))
                while k > 0:
                    if w1[-k:] == w2[:k]:
                        break
                    k -= 1
                
                self.cost[i][j] = k
        
        self.cache = {}
        ans = ''
        for i in range(n):
            candidate = self.dfs(A, i, (1 << n) - 1)
            if ans == '' or len(candidate) < len(ans):
                ans = candidate

        return ans
    
    def dfs(self, A, index, cur):
        if (index, cur) in self.cache:
            return self.cache[(index, cur)]

        if not ((1 << index) & cur):
            return ''
    
        if cur == (1 << index):
            return A[index]
        
        self.cache[(index, cur)] = ''
        for i in range(len(A)):
            if i == index or not ((1 << i) & cur):
                continue
            
            temp = self.dfs(A, i, cur - (1 << index)) + A[index][self.cost[i][index]:]
            if self.cache[(index, cur)] == '' or len(temp) < len(self.cache[(index, cur)]):
                self.cache[(index, cur)] = temp
        
        return self.cache[(index, cur)]

