class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        from collections import Counter 
        mods = [a % k for a in arr]
        
        c = Counter(mods)
        
        possible = True
        print(c)
        for val, ct in c.items():
            complement = (k - val) % k
            if complement == val:
                possible &= ct % 2 == 0
            else:
                possible &= c[complement] == ct
        return possible
