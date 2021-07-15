class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        
        #Approach 1:  use set 
        #The queue only contains boxes which is accessible
        q=collections.deque()
        
        #Important initiation,consider all opens box equivalent to they have keys
        keys_set=set([i for i in range(len(status)) if status[i]==1])   #Set for all available keys
        boxes_set=set(initialBoxes[:])  #set for all boxes that we have seen
        
        #Initialize the queue to process box
        for box in initialBoxes:
            if(box in keys_set):  #Status[box]==1 is equivalent to it has a key
                q.append(box)

        res=0
        visited=set()   #More universal for all test cases, record all the boxes that have been processed
        #use DFS to populate the queue
        while q:
            
            boxi=q.popleft()
            #Avoid duplicated count
            if(boxi in visited):
                continue
            else:
                visited.add(boxi)
                res +=candies[boxi]
                
            #Check all neighbors of current boxi
            for nei in containedBoxes[boxi]:
                if(nei in keys_set):  #it is either open or has key
                    q.append(nei)
                boxes_set.add(nei)
                
            #Check all keys of current boxi
            for key in keys[boxi]:
                #Only append the box index wich has not been considered, because there is no key, but it is in the boxes_set
                if(key in boxes_set and (key not in keys_set)):
                    q.append(key) 
                keys_set.add(key)
                
        return res
    
    
        #Approach 2: use list
        
#         haskeys=status[:]
#         seen=[0]*len(status)
#         q=collections.deque()   #Only contains boxes that are accessible
        
#         for box in initialBoxes:
#             seen[box]=1
#             if(haskeys[box]):
#                 q.append(box)   #Include the one only accessible
                
#         res=0
#         visited=set()
#         while q:
            
#             boxi=q.popleft()
#             if(boxi in visited):
#                 continue
#             else:
#                 visited.add(boxi)
#                 res+=candies[boxi]
            
#             #Since eachbox is contained in one box at most
#             #it will not result in duplicated elements in q
#             for nei in containedBoxes[boxi]:
#                 seen[nei]=1
#                 if(haskeys[nei]): q.append(nei)
            
#             #Iterate through all available keys, 
#             #inlcude the box has been seen but doesn't have key to the queue
#             for key in keys[boxi]:
#                 if(seen[key] and haskeys[key]==0):  #Meaning it has not been included in queue
#                     q.append(key)
#                 haskeys[key]=1
        
#         return res
                    
                
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
            
            

