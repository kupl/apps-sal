class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        
        keylock={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'A':'a','B':'b','C':'c','D':'d','E':'e','F':'f'}
        
        m=len(grid)
        n=len(grid[0])
        
        #Find the start point and the bit representation of all keys
        keys_target=0
        for i in range(m):
            for j in range(n):
                if(grid[i][j]=='@'):
                    start=(i,j)
                elif(grid[i][j] in 'abcdef'):
                    keys_target=keys_target|(1<<keylock[grid[i][j]])
                    
       
        #Check if all keys have been acquired
        def keyAllAcquired(value):
            if((value & keys_target)==keys_target):
                return True
            else:
                return False
            
        #check if it can be passed and within the boundary
        def isMovable(i,j):
            if(0<=i<=m-1 and 0<=j<=n-1 and grid[i][j]!='#'):
                return True
            else:
                return False
    
        #State is defined as ((i,j),keyloc acquired)
        visited_states={(start,0)}
        q=collections.deque()
        q.append((start,0))
        
        
        #Use DFS to find the minimum paths to cover all available keys
        step=0
        while q:
            #
            q_len=len(q)
            #Pop q_len number of elements from left of q
            for _ in range(q_len):
                (i,j),keys=q.popleft()
                #Return whenever all the keys in the grid are acquired
                if(keyAllAcquired(keys)):
                    return step
                
                #Move along 4 directions
                directs=[-1,0,1,0,-1]
                for d in range(4):
                    newi=i+directs[d]
                    newj=j+directs[d+1]
                    
                    #Before updating the state, check if the newi and newj is within the bound and don't hit
                    #the wall
                    if(isMovable(newi,newj)):
                        #Check the following cases and make the move
                        #Do nothing for other cases
                        #keys
                        if(grid[newi][newj] in 'abcdef'):
                            new_state=((newi,newj),keys|1<<keylock[grid[newi][newj]])
                            #check existence only for key
                            if(new_state not in visited_states):
                                visited_states.add(new_state)
                                q.append(new_state)
                        #locks 
                        elif(grid[newi][newj] in 'ABCDEF'):
                            lower_int=keylock[keylock[grid[newi][newj]]]
                            new_state=((newi,newj),keys|1<<(lower_int+6))
                            #Check key and exisitence for lock
                            if(keys & (1<<lower_int) and new_state not in visited_states):
                                visited_states.add(new_state)
                                q.append(new_state)
                                
                        #'.' or '@'     
                        elif(grid[newi][newj] in '.@' and ((newi,newj),keys) not in visited_states):
                            visited_states.add(((newi,newj),keys))
                            q.append(((newi,newj),keys))
            step+=1

        return -1
            
                           
                           
                           
                            
                            
                            
                    
                
            
            
        
        
        
        

