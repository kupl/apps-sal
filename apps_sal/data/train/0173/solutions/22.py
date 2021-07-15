from collections import defaultdict

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        n: int = len(arr)
            
        # Get the modulus of each value
        # we want to combine the mods so that they equal the target
        mods = {ix: 0 for ix in range(k)}
        
        for val in arr:
            mods[val % k] += 1
        
        # Need pairs for 0 mod
        if mods[0] % 2 != 0:
            return False
        
        # We need an equal number of complimenting pairs for
        # each value
        for mod in range(1, k):
            
            comp = (k - mod)

            # print(f'mod: {mod}   comp: {comp}')
            # print(f'mods: {mods}')

            if mods[comp] != mods[mod]:
                return False                
    
        return True
