# 
class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        # index for lights that should be on but is currently off
        pending_on = set()
        
        # index for lights that is turned on but not yet blue
        already_on = set()
        
        count = 0
        for idx, lgt in enumerate(light):
            lgt -= 1 # change from 1-base to 0-base
            if idx in already_on:
                already_on.remove(idx)
            else:
                pending_on.add(idx)
            
            if lgt in pending_on:
                pending_on.remove(lgt)
            else:
                already_on.add(lgt)
            
            if len(pending_on) == 0:
                count += 1
        
        return count

