class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n,m = len(grid),len(grid[0])
        root = {(i,j):(i,j) for i in range(n) for j in range(m)}   
        rank = collections.defaultdict(int)
        def find(x):
            if root[x]==x:
                return x
            root[x] == find(root[x])
            return root[x]
        
        def union(a,b):
            ra,rb = find(a),find(b)
            if ra!=rb:
                if rank[rb]>rank[ra]:
                    root[ra] = rb
                else:
                    root[rb] = ra
                    if rank[ra]==rank[rb]:
                        rank[ra]+=1
                
                
        
        for i in range(n):
            for j in range(m):
                #print(i,j)
                val = grid[i][j]
                # parent: i-1,j and i,j-1
                if i>0 and j>0 and grid[i-1][j] == grid[i][j-1]==val and find((i-1,j))==find((i,j-1)):
                    #print(find((i-1,j)),find((i,j-1)))
                    return True
                for ni,nj in [(i-1,j),(i,j-1)]:
                    if 0<=ni<n and 0<=nj<m and grid[ni][nj]==val:
                        #print((i,j),(ni,nj),val,grid[ni][nj])
                        union((i,j),(ni,nj))
                        #print(find((ni,nj)))
                
        return False

