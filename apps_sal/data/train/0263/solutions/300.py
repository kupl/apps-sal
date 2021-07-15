class Solution:
    
    def distinctNumbers(self, start, moves, validMoves, cache):
        if moves == 1:
            return 1
        
        if (start, moves) in cache:
            return cache[(start,moves)]
        
        result = 0
        for i in validMoves[start]:
            result += self.distinctNumbers(i, moves-1, validMoves, cache)
        cache[(start, moves)] = result
        
        return result
        
    def knightDialer(self, n: int) -> int:
        
        '''
        define numpad
        define validmove (within array and not 'X')
        use dynamic programming, grid of numbers and length n
        '''
        
        validMoves = dict()
        validMoves[1] = [6,8]
        validMoves[2] = [7,9]
        validMoves[3] = [4,8]
        validMoves[4] = [3,9,0]
        validMoves[5] = []
        validMoves[6] = [1,7,0]
        validMoves[7] = [2,6]
        validMoves[8] = [1,3]
        validMoves[9] = [2,4]
        validMoves[0] = [4,6]
        
        cache = {}
        
        
        result = 0
        for i in range(10):
            result += self.distinctNumbers(i, n, validMoves, cache)
            
        return result % (10 ** 9 + 7)
        
    
        
        
        

