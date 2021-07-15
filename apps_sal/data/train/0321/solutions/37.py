class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        def helper(d1, d2):
            s=0
            for c in 'abcdefghijklmnopqrstuvwxyz':
                s+=d1[c]-d2[c]
                
                if s<0:
                    return False
            return True
        
        c1=collections.Counter(s1)
        c2=collections.Counter(s2)
        return helper(c1,c2) or helper(c2,c1)
