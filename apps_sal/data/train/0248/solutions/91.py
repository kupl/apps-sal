class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        
        return self.unionfind(grid)
        
        '''
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        self.visited = set()
        
        for i in range(self.m):
            for j in range(self.n):
                
                if (i,j) not in self.visited:
                    if self.bfs((i,j), (-1,-1)):
                        return True
        return False

        '''
                
    def find(self, node):
        if self.parent[node[0]][node[1]] == node:
            return node
        else:
            p = self.find(self.parent[node[0]][node[1]])
            self.parent[node[0]][node[1]] = p
            return(p)
    
    def union(self, node1, node2):
        
        p1 = self.find(node1)
        p2 = self.find(node2)
        
        if self.rank[p1[0]][p1[1]] > self.rank[p2[0]][p2[1]]:
            self.parent[p2[0]][p2[1]] = p1
        elif self.rank[p2[0]][p2[1]] > self.rank[p1[0]][p1[1]]:
            self.parent[p1[0]][p1[1]] = p2
        else:
            self.parent[p1[0]][p1[1]] = p2
            self.rank[p2[0]][p2[1]] += 1
    
    def unionfind(self,g):
        
        nrow, ncol = len(g), len(g[0])
        
        self.parent = []
        self.rank = [[1]*ncol for _ in range(nrow)]
        
        for i in range(nrow):
                self.parent.append([(i,j) for j in range(ncol)])
        
        for i in range(nrow):
            for j in range(ncol):
                
                if i+1 < nrow and g[i][j] == g[i+1][j]:
                    
                    if self.find((i,j)) == self.find((i+1, j)):
                        return True
                    self.union((i,j), (i+1, j))
                
                if j+1 < ncol and g[i][j] == g[i][j+1]:
                    if self.find((i,j)) == self.find((i, j+1)):
                        return True
                    self.union((i,j), (i, j+1))
        return False
        
    
    def cycle(self, current, parent):
        
        if current in self.visited:
            return True
        
        self.visited.add(current)
        i,j = current
        neb = [(i+1,j), (i-1,j), (i, j+1), (i, j-1)]
        
        for ne in neb:
            ni, nj = ne
            if ne != parent and ni >= 0 and ni < self.m  and nj >=0 and nj < self.n and self.grid[ni][nj] == self.grid[i][j]:
                #print(ne)
                if self.cycle((ni, nj), current):
                    return True
        return False
                
    
    def bfs(self, current, parent):
        
        if current in self.visited:
            return True
        
        q = []
        q.append((current, parent))
        self.visited.add(current)
        
        while q:
            
            node, par = q.pop()
            #print(node)
            #print(par)
            i,j = node
            neb = [(i+1,j),(i-1,j), (i, j+1), (i,j-1)]
            
            for ni,nj in neb:
                if ni >= 0 and ni < self.m and nj >=0 and nj < self.n and self.grid[ni][nj] == self.grid[i][j] and (ni, nj) != par:
                    
                    if (ni, nj) in self.visited:
                        return True
                    q.append(((ni,nj), (i,j)))
                    self.visited.add((ni,nj))
        return False
                        
            
            
            
        
                

