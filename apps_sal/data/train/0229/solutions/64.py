from collections import Counter

class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        
        negs = [a for a in A if a < 0]
        pos = [a for a in A if a > 0]
        zeros = [a for a in A if a == 0]
        
        if any(map(lambda x: len(x) % 2 != 0, [negs, pos, zeros])):
            return False
        
        if not self.is_valid(negs, True) or not self.is_valid(pos, False):
            return False
        return True
        
    
    def is_valid(self, A, neg=False):
        A = sorted(A)
        N = len(A)
        
        if neg:
            A = A[::-1]

        c = Counter(A)
        for a in A:
            if c[a] == 0:
                continue
            target = a * 2
            if c[target] == 0:
                return False
            c[a] -= 1
            c[target] -= 1
        return True
