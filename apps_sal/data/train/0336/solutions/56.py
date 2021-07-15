from collections import defaultdict
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq = defaultdict(int)
        for char in s:
            freq[char] += 1
        
        for char in t:
            if freq[char] > 0:
                freq[char] -= 1
        
        return sum(freq.values())
