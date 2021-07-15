class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        
        #Approach 1:  use set 
        #The queue only contains boxes which is accessible
#         q=collections.deque()
#         keys_set=set()   #Set for all available keys
#         boxes_set=set()  #set for all un-opened boxes
        
#         #Initialize the queue to process box
#         for box in initialBoxes:
#             if(status[box]==1 or box in keys_set):  #Check if this box is open or there is key available
#                 q.append(box)
#                 for key in keys[box]:
#                     keys_set.add(key)
#                     if(key in boxes_set):           #Check if the new key can open a box in boxes_set
#                         q.append(key)
#                         boxes_set.remove(key)
#             else:
#                 boxes_set.add(box)
                

#         res=0
#         visited=set()
        
#         #use DFS to populate the queue
#         while q:
            
#             boxi=q.popleft()
#             #Avoid duplicated couting of candies
#             if(boxi in visited):
#                 continue
#             else:
#                 visited.add(boxi)
#                 res +=candies[boxi]
                
#             #Check all neighbors of current boxi
#             for nei in containedBoxes[boxi]:
#                 if(status[nei]==1 or nei in keys_set):   #Check if this box is open or there is a key for this box
#                     q.append(nei)
#                     for key in keys[nei]:
#                         keys_set.add(key)
#                         if(key in boxes_set):             #check if the new key can open a box in boxes_set
#                             q.append(key)
#                             boxes_set.remove(key)
#                 else:
#                     boxes_set.add(nei)
        
#         return res
    
    
        #Approach 2: use list
        
        haskeys=status[:]
        seen=[0]*len(status)
        q=collections.deque()   #Only contains boxes that are accessible
        
        for box in initialBoxes:
            seen[box]=1
            if(haskeys[box]):
                q.append(box)   #Include the one only accessible
                
        res=0
        while q:
            
            boxi=q.popleft()
            res+=candies[boxi]
            
            #Since eachbox is contained in one box at most
            #it will not result in duplicated elements in q
            for nei in containedBoxes[boxi]:
                seen[nei]=1
                if(haskeys[nei]): q.append(nei)
            
            #Iterate through all available keys, 
            #inlcude the box has been seen but doesn't have key to the queue
            for key in keys[boxi]:
                if(seen[key] and haskeys[key]==0):  #Meaning it has not been included in queue
                    q.append(key)
                haskeys[key]=1
        
        return res
                    
                
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
            
            

