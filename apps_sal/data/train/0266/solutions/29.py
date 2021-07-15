class Solution:
    def numSplits(self, s: str) -> int:
        initial = {}
        
        for char in s:
            if char in initial:
                initial[char] += 1
            else:
                initial[char] = 1
            
        other = {}
        output = 0
        
        for char in s:
            initial[char] -= 1
            if initial[char] == 0:
                del initial[char]
            other[char] = 1
            if len(initial) == len(other):
                output += 1
        return output
            

