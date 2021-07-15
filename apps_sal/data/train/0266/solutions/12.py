from collections import Counter

class Solution:
    def numSplits(self, s: str) -> int:
        prev_counter = {}
        post_counter = Counter(s)
        
        count = 0
        for partition in range(len(s)):
            prev, post = s[:partition], s[partition:]
            
            if not prev or not post:
                continue
            
            curr = prev[-1]
            if curr not in prev_counter:
                prev_counter[curr] = 0
                
            prev_counter[curr] += 1
            post_counter[curr] -= 1
            
            if post_counter[curr] == 0:
                post_counter.pop(curr)
            
            if len(prev_counter) == len(post_counter):
                count += 1
        
        return count
            

