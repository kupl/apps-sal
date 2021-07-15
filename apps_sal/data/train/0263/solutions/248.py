class Solution:
    legal_moves = {
            0: [4, 4],
            1: [6, 8],
            2: [7, 7],
            3: [4, 8],
            4: [0, 1, 7],
            # 5: [],
            6: [0, 1, 7],
            7: [2, 4],
            8: [1, 1],
            9: [2, 4]
        }
    
    def knightDialer(self, n: int) -> int:
        total = 0 if n != 1 else 1
        memo = {}
        for i in range(0, 10):
            if i is not 5:
                total = total + self.num_jumps(i, n - 1, memo)
                
        return total % (pow(10, 9) + 7)
            
    def num_jumps(self, start, jumps_left, memo):
        
        # If we have no moves left we have completed a number
        if jumps_left == 0:
            return 1
        
        # Check if we have done this calculation before
        if (start, jumps_left) not in memo:
            
            # Calculate total number of numbers from this starting position
            total = 0
            for legal_move in self.legal_moves[start]:
                total = total + self.num_jumps(legal_move, jumps_left - 1, memo)
        
            # Save result
            memo[(start, jumps_left)] = total
        
        # Return calculated or retreived result
        return memo[(start, jumps_left)]
