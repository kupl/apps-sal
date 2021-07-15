class Solution:
    # [22,57,74,79]
    def possibleForce (self,force, position):
        count = 0
        lastBall = 0
        for i in range (0,len(position)):
            if (i == 0 or (position[i]- position[lastBall]) >= force):
                count +=1
                lastBall =i
        return  count 
                
            
            
    def maxDistance(self, position: List[int], m: int) -> int:   
        position.sort()
        #print(position)
        maxReally = (position[-1] -position[0] )/ (m-1)
        #print (maxReally)
        maxForce = maxReally
        minForce = 1
        result = -1
        
        while (minForce <= maxForce and minForce >0 and maxForce <= maxReally):
            middleForce = minForce + (maxForce - minForce) // 2
            print((minForce, maxForce, middleForce))
            count =  self.possibleForce(middleForce, position)
            print (count)
            if count >= m:
                # go right
                minForce = middleForce + 1
                result = middleForce
            else:
                # go left
                maxForce = middleForce - 1

        return int(result )
                
                    
                
            
        
        
   
    
    #x o o x o o x - o x
            
             
             

