class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        #The queue only contains boxes which is accessible
        q=collections.deque()
        keys_set=set()   #Set for all available keys
        boxes_set=set()  #set for all un-opened boxes
        
        #Initialize the queue to process box
        for box in initialBoxes:
            if(status[box]==1 or box in keys_set):  #Check if this box is open or there is key available
                q.append(box)
                for key in keys[box]:
                    keys_set.add(key)
                    if(key in boxes_set):           #Check if the new key can open a box in boxes_set
                        q.append(key)
                        boxes_set.remove(key)
            else:
                boxes_set.add(box)
                

        res=0
        visited=set()
        
        #use DFS to populate the queue
        while q:
            
            boxi=q.popleft()
            #Avoid duplicated couting of candies
            if(boxi in visited):
                continue
            else:
                visited.add(boxi)
                res +=candies[boxi]
                
            #Check all neighbors of current boxi
            for nei in containedBoxes[boxi]:
                if(status[nei]==1 or nei in keys_set):   #Check if this box is open or there is a key for this box
                    q.append(nei)
                    for key in keys[nei]:
                        keys_set.add(key)
                        if(key in boxes_set):             #check if the new key can open a box in boxes_set
                            q.append(key)
                            boxes_set.remove(key)
                else:
                    boxes_set.add(nei)
        
        return res
                
            
            
            

