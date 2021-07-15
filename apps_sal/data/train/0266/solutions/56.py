from collections import Counter

class Solution:
    def numSplits(self, s: str) -> int:
        s1 = Counter()
        s2 = Counter(s)
        count = 0
        
        for a in s:
            s1[a] += 1
            s2[a] -= 1
            if s2[a] == 0:
                s2.pop(a)
            if len(s1) == len(s2):
                count += 1
        return count
