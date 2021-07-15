class Box():
    def __init__(self, status, candies, keys, boxes):
        self.status = status
        self.candies = candies
        self.keys = keys
        self.containedBoxes = boxes

def openboxes(unopened, keys, Q):
    for u in unopened:
        if u in keys:
            Q.append(u)
            unopened.remove(u)
    

class Solution:
            
    
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        mykeys = []
        unopened = []
        candySum = 0
        
        
        Q = []
        for i in initialBoxes:
            mykeys.extend(keys[i])
            if status[i] == 1:
                Q.append(i)
            else:
                unopened.append(i)
       
        openboxes(unopened,mykeys,Q)
        
        while Q != []:
            box = Q.pop(0)
            candySum += candies[box]
            
            
            for b in containedBoxes[box]:
                mykeys.extend(keys[b])
                if status[b] == 1:
                    Q.append(b)
                else:
                    unopened.append(b)
            
            openboxes(unopened, mykeys, Q)
                    
                    
        
        return candySum
                    
            

