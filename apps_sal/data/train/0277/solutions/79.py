class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        s = 0
        max_index = 0
        count = 0
        for i in range(len(light)):
            s += 1
            if light[i] > max_index:
                max_index = light[i]
            
            #print(f\"s: {s} max_index: {max_index} i: {i}\")
            if i+1 == max_index:
                count += 1
                
        return count
