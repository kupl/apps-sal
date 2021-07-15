class Solution:
    def __init__(self):
        self.moves = [
            [4,6],
            [6,8],
            [7,9],
            [4,8],
            [3,9,0],
            [],
            [7,1,0],
            [6,2],
            [1,3],
            [4,2]
        ]
        
        self.memoized_moves = {}
    
    def knightDialer(self, n: int) -> int:
        moves = 0
        for i in range(10):
            moves += self.getNumberFromNMoves(n-1, i)
        
        return moves%(pow(10,9) + 7)
        
    
    def getNumberFromNMoves(self, remaining_moves, current_number):
        if remaining_moves == 0:
            return 1
        
        moves = 0
        for move in self.moves[current_number]:
            if (move, remaining_moves) not in self.memoized_moves:
                self.memoized_moves[(move, remaining_moves)] = self.getNumberFromNMoves(remaining_moves-1, move)
            moves += self.memoized_moves[(move, remaining_moves)]
            
        return moves
        
    
    def getMoves(self, number):
        return self.moves[number]
        
        

