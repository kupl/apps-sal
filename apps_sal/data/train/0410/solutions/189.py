class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        self.visited = {}
        
        def recur(n):
            if n in self.visited:
                return self.visited[n]
            if n == 1:
                return 0
            else:
                if n%2 == 0:
                    moves = 1 + recur(int(n/2))
                else:
                    moves = 1 + recur(int(3*n)+1)
                self.visited[n]=moves
                return self.visited[n]
        for i in range(hi,lo-1,-1):
            if i not in self.visited:
                self.visited[i]=recur(i)
            
        result =  [ (x,self.visited[x]) for x in self.visited if lo <=x and x<=hi]
        result.sort(key = lambda x : (x[1],x[0]))
        return result[k-1][0]
