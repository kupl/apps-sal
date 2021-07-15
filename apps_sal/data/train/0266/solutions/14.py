from collections import defaultdict, Counter

class Solution:
    def numSplits(self, s: str) -> int:
        len_s = len(s)
        if len_s == 0:
            return 0
        
        if len_s == 1:
            return 1
        
        nb_good_splits = 0
        left_counter = defaultdict(int)
        right_counter = Counter(s)
        
        for i in range(1, len_s):
            left, right = s[0:i], s[i:]
            swing_letter = left[-1]
            
            left_counter[swing_letter] += 1
            right_counter[swing_letter] -= 1
            
            if right_counter[swing_letter] == 0:
                del right_counter[swing_letter]
            
            if len(left_counter) == len(right_counter):
                nb_good_splits += 1
                
        return nb_good_splits

