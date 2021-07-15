class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t): return False
        
        moves = collections.Counter()
        
        for si, ti in zip(s, t):
            shifts = (ord(ti) - ord(si)) % 26
            moves[shifts] += 1
        
        for i in range(1, 26):
            total_moves = moves[i]
            
            if i + 26*(total_moves-1) > k: return False
        
        return True
