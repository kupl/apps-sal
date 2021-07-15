import collections

class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        n = len(light)
        ans = count_blue = 0
        state = collections.defaultdict(int)
        
        for j, bulb in enumerate(light):
            #if prev bulb is blue
            if bulb == 1 or state[bulb-1]==2:
                state[bulb] = 2
                count_blue+=1
            else:
                # else just set to lit
                state[bulb] = 1
            
            
            # if curre bulb is blue, set next bulb to blue if they are lit
            if state[bulb] == 2:
                i = bulb+1
                while i<n+1 and state[i]==1:
                    count_blue+=1
                    state[i] = 2
                    i+=1
            if count_blue== j+1:
                ans += 1
            
        return ans
                

