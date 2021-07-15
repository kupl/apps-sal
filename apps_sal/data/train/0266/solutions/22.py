class Solution:
    def numSplits(self, s: str) -> int:
        cnt = 0
        l_set = set()
        d = {c: s.count(c) for c in set(s)}
        
        for c in s:
            l_set.add(c)
            d[c] -= 1
            if d[c] == 0:
                d.pop(c, None)
            if len(l_set) == len(d):
                   cnt += 1
        return cnt
