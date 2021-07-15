class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        
        # rearange s1 in smallest possible ordering
        # reaarange s2 in largest possible ordering
        
        # vice versa
        
        s1 = list(s1)
        s2 = list(s2)
        
        s1.sort(reverse=True)
        s2.sort(reverse=True)
        
        match =  all(x>=y for x, y in zip(s1, s2))
        if match: return True
        
        s1.sort()
        s2.sort()
        match = all(y>=x for x, y in zip(s1, s2))
        return match
