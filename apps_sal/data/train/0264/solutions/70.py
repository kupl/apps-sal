class Solution:
    def maxLength(self, l: List[str]) -> int:
        selected = set()
        
        def ok(word, s) -> bool:
            return not any(v in s for v in word) and len(word) == len(set(word))
        
        def backTrack(l: List[str], curr_index: int, selected: set) -> int:
            maxLength = 0
            
            if curr_index != -1:
                for v in l[curr_index]: # add the chosen word to selected
                    selected.add(v)
            
            for i in range(curr_index+1,len(l)):
                if ok(l[i],selected): # word is good - so we choose it
                    
                    maxLength = max(maxLength, len(l[i])
                                    + backTrack(l, i, selected.copy()))
                                        
            return maxLength
        
        return backTrack(l, -1, selected)
