from heapq import *

class Solution:
    def lastSubstring(self, s: str) -> str:
        maxc = max(s)
        layer = []
        for i, c in enumerate(s):
            if c == maxc:
                layer.append((c, i, i)) # (char, cur, start)
                
        N = len(s)
        ss = set(i for _,_,i in layer)
        while len(layer) > 1:
            nc = max(s[j+1] for _, j, i in layer if j+1 < N)
            newlayer = []
            todelete = set()
            for _, j, i in layer:
                if j+1 < N and s[j+1] == nc and j+1 in ss:
                    todelete.add(j+1)
            for _, j, i in layer:
                if j+1 < N and s[j+1] == nc and i not in todelete:
                    newlayer.append((nc, j+1, i))
            layer = newlayer
        
        _, cur, start = layer[0]
        return s[start:]
        

