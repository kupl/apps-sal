class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        perm1 = sorted(list(s1))
        perm2 = sorted(list(s2))
        zipped = zip(perm1,perm2)
        
        forward = True
        backward = True
        
        for x, y in zipped:
            if ord(x) > ord(y):
                forward = False
                
            if ord(y) > ord(x):
                backward = False
                
            
        return forward or backward
