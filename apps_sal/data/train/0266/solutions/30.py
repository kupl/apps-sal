from collections import defaultdict
class Solution:
    def numSplits(self, s: str) -> int:
        hmap = defaultdict(int)
        for ele in s:
            hmap[ele]+=1
        
        
        count = 0
        size = len(hmap)
        
        second_map = defaultdict(int)
        for i in range(len(s)):
            c = s[i]
            second_map[c]+=1
            hmap[c]-=1
            if hmap[c] == 0:
                del hmap[c]
            if len(second_map) == len(hmap):
                count+=1
            elif len(second_map) > len(hmap):
                break
        
        
        return count
        

