class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        # Moments at which max light is last consec on
        max_light_on = -1
        last_consecutive_on = -1
        
        all_blue = 0
        
        for light_bulb in light:
            # Turn this light on by negating it
            light_index = abs(light_bulb) - 1
            light[light_index] = -light[light_index]
            
            # Check if this is the max light on
            max_light_on = max(max_light_on, light_index)
            
            # Check if this is the last consecutive light on starting from 0
            while last_consecutive_on < len(light) - 1 and light[last_consecutive_on + 1] < 0:
                last_consecutive_on += 1
            
            if max_light_on == last_consecutive_on:
                all_blue += 1
        
        return all_blue
