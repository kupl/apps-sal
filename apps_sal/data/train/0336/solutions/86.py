class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sd = {}
        td = {}
        for c in s:
            if sd.get(c):
                sd[c] += 1
            else:
                sd[c] = 1
                
        count = 0
        for c in t:
            if sd.get(c) and sd[c] > 0:
                sd[c] -= 1
            else:
                count += 1
        return count
