from functools import lru_cache

def failure(pat):
    i, target, n = 1, 0, len(pat)
    res = [0]
    while i < n:
        if pat[i] == pat[target]:
            target+=1
            res.append(target)
            i += 1
        elif target:
            target = res[target-1]
        else:
            res.append(0)
            i+=1
    return res
            
def srange(a, b):
    yield from (chr(i) for i in range(ord(a), ord(b) + 1))

class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        f = failure(evil)
        @lru_cache(None)
        def dfs(idx, max_matched=0, lb=True, rb=True):
            
            if max_matched == len(evil): return 0
            if idx == n: return 1
            
            l = s1[idx] if lb else 'a'
            r = s2[idx] if rb else 'z'
            candidates = [*srange(l, r)]
            
            res = 0
            for i, c in enumerate(candidates):
                next_match = max_matched 
                while next_match and evil[next_match] != c:
                    next_match = f[next_match-1]
                res += dfs(idx+1, next_match + (c == evil[next_match]), 
                          lb = (lb and i == 0), rb = (rb and i == len(candidates) -1))
            
            return res
        return dfs(0) % (10**9 + 7)
