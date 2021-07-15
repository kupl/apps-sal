class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        moves = defaultdict(lambda: 0) 
        K_div = k // 26
        K_mod = k % 26
        
        if len(s) != len(t):
            return False
        
        for cs, ct in zip(s, t):
            ordc = ord(cs)
            ordt = ord(ct)
            
            move = ordt - ordc 
            if move < 0:
                move += 26
            
            if move == 0:
                continue
                
            numMoves = K_div + (1 if move <= K_mod else 0) 
            
            if moves[move] == numMoves:
                return False
            
            moves[move] += 1
            
        return True
