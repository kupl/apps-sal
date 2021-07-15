class Solution:
    moves = {0: [4, 6], 1: [6, 8], 2: [7, 9],
            3: [4, 8], 4: [0,3,9], 5:[], 6:[0, 1, 7], 
             7: [2, 6], 8: [1, 3], 9: [2, 4]}
    
    def dialed_Numbers(self, number, moves_left, memoization):
        if (number, moves_left) in memoization:
            return memoization[(number, moves_left)]
        
        if moves_left == 0:
            return 1
        
        fin_sum = 0
        for next_move in self.moves[number]:
            fin_sum += self.dialed_Numbers(next_move, moves_left - 1, memoization)
            
        memoization[(number, moves_left)] = fin_sum
        return fin_sum
    
    def knightDialer(self, n: int) -> int:
        memoization = {}
        fin_sum = 0
        for i in range(0, 10):
            fin_sum += (self.dialed_Numbers(i, n-1, memoization))
        
        return fin_sum % (10**9 + 7)
