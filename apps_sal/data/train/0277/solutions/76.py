class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        status = [0]*(len(light)+1)
                    
        k = 0
        number_of_blues = 0
        count = 0
        
        while(k < len(light)):
            idx = light[k]
            status[idx] = 1
            
            if idx == 1:
                status[1] = 2
                number_of_blues += 1
                
            for i in range(idx,len(light)+1):
                if i == idx and status[i] == 2:
                    continue
                if status[i] == 1 and status[i-1] == 2:
                    status[i] = 2
                    number_of_blues += 1
                else:
                    break
                    
            if number_of_blues == k+1:
                count += 1


            #print(status)   
            k += 1

        return count
            
                
                
                

