class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m=len(grid)
        n=len(grid[0])
        
        def neighbor(i,j, keys):
            res=[]
            keys_list = list(keys)
            if grid[i][j] in ['.', '@']:
                res.append((i,j,keys))
            elif grid[i][j].islower():
                if grid[i][j] in keys_list: # already picked key, treat as empty cell
                    res.append((i,j,keys))
                else: # pick up new key
                    keys_list.append(grid[i][j])
                    new_keys=''.join(keys_list)
                    res.append((i,j,new_keys))
            elif grid[i][j].isupper():
                if grid[i][j].lower() in keys_list: # treat lock as empty cell if have the key
                    res.append((i,j,keys))
            return res
        
        def move(i,j,keys):
            nexts=[]
            if i>0:
                nei = neighbor(i-1,j,keys)
                if nei:
                    nexts += nei
            if i<m-1:
                nei=neighbor(i+1,j,keys)
                if nei:
                    nexts += nei
            if j>0:
                nei=neighbor(i,j-1,keys)
                if nei:
                    nexts += nei
            if j<n-1:
                nei= neighbor(i,j+1,keys)
                if nei:
                    nexts += nei
            return nexts
                  
        def get_start_and_keys():
            x, y, keys = -1, -1, 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j]=='@':
                        x, y = i, j
                    elif grid[i][j].islower():
                        keys +=1
            return x, y, keys
        
        i0, j0, total_keys = get_start_and_keys()
        q=deque()
        start_point = (i0, j0, '')
        q.append(start_point)
        visited=set()
        visited.add(start_point)
        steps = -1
        while q:
            size=len(q)
            steps +=1
            for x in range(size):
                pop=q.popleft()
                i=pop[0]
                j=pop[1]
                keys=pop[2]
                if len(keys)==total_keys:
                    return steps
                for nex in move(i,j,keys):
                    if nex not in visited:
                        q.append(nex)
                        visited.add(nex)
        return -1
       
                
                
                
                
                
                
        
        
        

