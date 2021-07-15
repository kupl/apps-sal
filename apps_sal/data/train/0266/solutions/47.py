class Solution:
    def numSplits(self, s: str) -> int:
        left = {s[0]:1}
        right = {}
        for i in range(1, len(s)):
            right[s[i]] = right.get(s[i], 0) + 1
            
        #check if the left set has as many items as the right set
        #then we incremenet the middle pointer
        #remove the item from right
        #add it to left
        middle_i = 1
        count = 0
        while middle_i < len(s):
            if len(left) == len(right):
                count += 1
                
            middle = s[middle_i]
            right[middle] -= 1
            if right[middle] == 0:
                right.pop(middle)
            
            left[middle] = left.get(middle, 0) + 1
            
            middle_i += 1
        
        return count

