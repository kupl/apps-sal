class Solution:
    def numSplits(self, s: str) -> int:
        set_f = set()
        map_b = defaultdict(int)
        
        for c in s:
            map_b[c] += 1
         
        num = 0
        for c in s:
            map_b[c] -= 1
            if not map_b[c]:
                del map_b[c]
                
            set_f.add(c)
            
            if len(set_f) == len(map_b):
                num += 1
                
        return num
