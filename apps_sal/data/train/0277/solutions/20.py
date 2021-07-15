class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        
        
        cnt = 0
        checker =  0
        light_status = 0
        
        for i in range(0, len(light)):
            light_status |= 1 <<(light[i] - 1)
            
            checker |= 1 << i
            
            if checker == light_status:
                cnt+=1
        return cnt
            
        

