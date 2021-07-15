class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        numodds = 0
        keys = collections.defaultdict(int)
        for c in s:
            keys[c] += 1
        
        for key in keys:
            if keys[key] % 2:
                numodds += 1
        
        return numodds <= k
