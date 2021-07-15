class Solution:
    def shortestPathAllKeys(self, grid):
        m,n,k,keys,d=len(grid),len(grid[0]),0,'',set()
        grid.append('#'*n)
        for i in range(m): grid[i]+='#'
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='@': si,sj=i,j
                elif grid[i][j] in 'abcdef': keys+=grid[i][j]
        a,keyss=[(si,sj,keys)],''.join([c.upper() for c in keys])
        while a:
            b=[]
            for i,j,keys in a:
                #if grid[i][j] in keys: keys = keys.replace(grid[i][j], '')# keys=''.join([c for c in keys if c!=grid[i][j]])
                keys = keys.replace(grid[i][j], '')# keys=''.join([c for c in keys if c!=grid[i][j]])
                if not keys: return k
                for ii,jj in (i,j+1),(i+1,j),(i,j-1),(i-1,j):
                    if grid[ii][jj]!='#' and (not(grid[ii][jj] in keyss and grid[ii][jj].lower() in keys)) and ((ii,jj,keys) not in d):
                        d.add((ii,jj,keys))
                        b.append((ii,jj,keys))
            a,k=b,k+1
        return -1
